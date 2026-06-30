"""
main.py
-------
Orquestrador do fluxo completo do sistema RAG-EJCM.

Fluxo:
    1. Carrega personas (stakeholders simulados) de personas.json
    2. Para cada persona, o SimuladorStakeholder gera requisitos individuais
    3. Todos os requisitos são alimentados ao ConsolidadorRequisitos,
       que também consulta a base de conhecimento via RAG
    4. Produz um documento único de requisitos finais

    [personas.json]
          ↓
    [Simulador] x N personas → requisitos por persona
          ↓
    [Consolidador] ← contexto do RAG
          ↓
    requisitos_consolidados.md
"""

from __future__ import annotations

import argparse
import json
import logging
import time
from pathlib import Path

from agents import ConsolidadorRequisitos, SimuladorStakeholder

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s - %(name)s - %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("main")

BASE_DIR = Path(__file__).parent.resolve()
PERSONAS_JSON = BASE_DIR / "personas.json"
REQUISITOS_INDIVIDUAIS_JSON = BASE_DIR / "requisitos_individuais.json"
DOCUMENTO_FINAL_MD = BASE_DIR / "requisitos_consolidados.md"

DELAY_ENTRE_PERSONAS_S = 5  # rate-limit suave entre chamadas ao Gemini
QUERY_RAG_PADRAO = (
    "contexto institucional da EJCM, processos organizacionais, "
    "gestão de projetos, membros e documentos"
)


def carregar_personas() -> dict:
    """Carrega as descrições das personas a partir de `personas.json`.

    Returns:
        Dicionário `{nome_persona: descricao_persona}`.

    Raises:
        FileNotFoundError: Se o arquivo `personas.json` não existir.
    """
    if not PERSONAS_JSON.exists():
        raise FileNotFoundError(
            f"Arquivo {PERSONAS_JSON.name} não encontrado. "
            "Ele deve conter as descrições das personas."
        )
    with PERSONAS_JSON.open("r", encoding="utf-8") as f:
        return json.load(f)


def gerar_requisitos_individuais(
    personas: dict,
    simulador: SimuladorStakeholder,
    delay_s: float = DELAY_ENTRE_PERSONAS_S,
) -> dict:
    """Executa o Simulador para cada persona e coleta seus requisitos.

    Args:
        personas: Dicionário `{nome: descricao}`.
        simulador: Instância de `SimuladorStakeholder`.
        delay_s: Espera entre chamadas (suaviza rate-limit da API).

    Returns:
        Dicionário `{nome_persona: requisitos_gerados}`.
    """
    requisitos_por_persona: dict[str, str] = {}
    total = len(personas)

    for i, (nome, descricao) in enumerate(personas.items(), start=1):
        logger.info("[%d/%d] Gerando requisitos para: %s", i, total, nome)
        requisitos = simulador.gerar_requisitos(descricao)
        requisitos_por_persona[nome] = requisitos

        if i < total and delay_s > 0:
            time.sleep(delay_s)

    # Persiste para auditoria/reprocessamento
    with REQUISITOS_INDIVIDUAIS_JSON.open("w", encoding="utf-8") as f:
        json.dump(requisitos_por_persona, f, ensure_ascii=False, indent=2)
    logger.info("Requisitos individuais salvos em %s",
                REQUISITOS_INDIVIDUAIS_JSON.name)

    return requisitos_por_persona


def carregar_requisitos_individuais(caminho: Path) -> dict:
    """Carrega requisitos individuais já gerados (modo skip-simulator).

    Args:
        caminho: Caminho do JSON com `{nome_persona: requisitos}`.

    Returns:
        Dicionário com os requisitos por persona.
    """
    if not caminho.exists():
        raise FileNotFoundError(
            f"Arquivo {caminho} não encontrado. Gere-o rodando o simulador "
            "ou forneça um JSON com `{nome_persona: requisitos}`."
        )
    with caminho.open("r", encoding="utf-8") as f:
        return json.load(f)


def parse_args() -> argparse.Namespace:
    """Define e processa argumentos de linha de comando."""
    parser = argparse.ArgumentParser(
        description="Pipeline RAG-EJCM: personas → simulador → consolidador."
    )
    parser.add_argument(
        "--skip-simulator",
        action="store_true",
        help=(
            "Pula a etapa do simulador e carrega requisitos já prontos "
            "de --requisitos (padrão: requisitos_individuais.json)."
        ),
    )
    parser.add_argument(
        "--requisitos",
        type=Path,
        default=REQUISITOS_INDIVIDUAIS_JSON,
        help=(
            "Caminho do JSON com requisitos já gerados "
            f"(default: {REQUISITOS_INDIVIDUAIS_JSON.name})."
        ),
    )
    parser.add_argument(
        "--query-rag",
        default=QUERY_RAG_PADRAO,
        help="Consulta usada para buscar contexto no RAG.",
    )
    parser.add_argument(
        "--top-k",
        type=int,
        default=5,
        help="Número de trechos recuperados do RAG (default: 5).",
    )
    return parser.parse_args()


def main() -> None:
    """Executa o pipeline RAG-EJCM.

    Modos:
        * Padrão: personas → simulador → consolidador
        * --skip-simulator: carrega requisitos prontos → consolidador
    """
    args = parse_args()
    logger.info("=== Iniciando pipeline RAG-EJCM ===")

    # 1) Requisitos por persona (gerados ou carregados)
    if args.skip_simulator:
        logger.info("Modo SKIP-SIMULATOR: carregando requisitos de %s",
                    args.requisitos.name)
        requisitos_por_persona = carregar_requisitos_individuais(args.requisitos)
        logger.info("Requisitos carregados para %d personas: %s",
                    len(requisitos_por_persona),
                    list(requisitos_por_persona.keys()))
    else:
        personas = carregar_personas()
        logger.info("Personas carregadas (%d): %s",
                    len(personas), list(personas.keys()))
        simulador = SimuladorStakeholder(model="gemini-3.5-flash")
        requisitos_por_persona = gerar_requisitos_individuais(
            personas, simulador
        )

    # 2) Consolidador — unifica tudo em um documento final
    logger.info("Consolidando requisitos com apoio do RAG...")
    consolidador = ConsolidadorRequisitos(model="gemini-3.5-flash")
    documento_final = consolidador.consolidar(
        requisitos_por_persona=requisitos_por_persona,
        query_rag=args.query_rag,
        top_k=args.top_k,
    )

    # 3) Saída
    print("\n" + "=" * 70)
    print(" DOCUMENTO FINAL CONSOLIDADO ")
    print("=" * 70 + "\n")
    print(documento_final)
    print("\n" + "=" * 70)

    DOCUMENTO_FINAL_MD.write_text(documento_final, encoding="utf-8")
    logger.info("Documento final salvo em %s", DOCUMENTO_FINAL_MD.name)
    logger.info("=== Pipeline concluído ===")


if __name__ == "__main__":
    main()
