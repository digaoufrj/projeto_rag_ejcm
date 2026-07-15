"""
agents/simulador.py
-------------------
Agente Simulador de Stakeholders.

Recebe a descrição de uma persona (stakeholder simulado) e gera os
requisitos de software correspondentes, respeitando o contexto da Empresa Júnior.

Autoria original: Giovanna / Cássio (adaptado para integrar ao projeto).
"""

from __future__ import annotations

import logging
import os
from typing import Optional

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

logger = logging.getLogger("agente_simulador")


class SimuladorStakeholder:
    """Agente LLM que simula um stakeholder e gera requisitos a partir de uma persona."""

    PROMPT_SISTEMA = """
Você é um agente simulador de stakeholders para processos de Engenharia de Requisitos.

Sua função é interpretar fielmente a persona descrita pelo usuário e gerar requisitos de software que representem as necessidades, expectativas e restrições desse stakeholder.

## Contexto
A organização é uma Empresa Júnior de Consultoria e Microinformática.
Será desenvolvido um sistema integrado e centralizado para apoiar a gestão interna da Empresa Júnior. O sistema deverá permitir o gerenciamento de projetos, tarefas, membros, documentos e processos organizacionais.

A Empresa Júnior desenvolve soluções digitais seguindo as seguintes etapas:
- Pesquisa: levantamento e validação das necessidades dos clientes por meio de pesquisas de UX.
- Prototipação: criação de protótipos interativos das soluções.
- Desenvolvimento: implementação de aplicações web e móveis com foco em desempenho e escalabilidade.
- Entrega e suporte: implantação da solução e suporte contínuo para manutenção e evolução.

Os requisitos devem considerar esse contexto organizacional.

## Regras
- Analise cuidadosamente a persona fornecida.
- Gere requisitos exclusivamente com base na persona e no contexto apresentado.
- Não invente necessidades que não sejam compatíveis com o perfil da persona.
- Priorize requisitos que estejam relacionados às responsabilidades, objetivos e dificuldades do stakeholder.
- Sempre que apropriado, produza requisitos funcionais e não funcionais.
- Escreva requisitos claros, objetivos e verificáveis.
- Cada requisito deve representar uma necessidade distinta.
- Retorne apenas a lista de requisitos.
"""

    def __init__(
        self,
        model: str = "gemini-3.5-flash",
        temperature: float = 0.7,
        api_key: Optional[str] = None,
    ) -> None:
        """Inicializa o agente simulador.

        Args:
            model: Modelo Gemini a ser utilizado.
            temperature: Temperatura de geração (0.0 a 1.0).
            api_key: Chave da API. Se None, lê de GOOGLE_API_KEY no ambiente.
        """
        chave = api_key or os.getenv("GOOGLE_API_KEY")
        if not chave:
            raise EnvironmentError(
                "GOOGLE_API_KEY não encontrada. Defina no .env ou passe via api_key."
            )

        self.client = genai.Client(api_key=chave)
        self.model = model
        self.temperature = temperature

    def gerar_requisitos(self, persona: str) -> str:
        """Gera requisitos de software a partir da descrição de uma persona.

        Args:
            persona: Texto descrevendo o stakeholder (papel, perfil, objetivos etc.).

        Returns:
            Texto com a lista de requisitos gerados, ou mensagem de erro.
        """
        config = types.GenerateContentConfig(
            system_instruction=self.PROMPT_SISTEMA,
            temperature=self.temperature,
        )

        prompt_usuario = f"### Persona\n\n{persona}"

        try:
            resposta = self.client.models.generate_content(
                model=self.model,
                contents=prompt_usuario,
                config=config,
            )
            return resposta.text
        except Exception as exc:  # noqa: BLE001
            logger.error("Falha ao gerar requisitos: %s", exc, exc_info=True)
            return f"Erro ao gerar requisitos para a persona: {exc}"


if __name__ == "__main__":
    import json
    import time
    from pathlib import Path

    logging.basicConfig(level=logging.INFO)

    personas_path = Path(__file__).parent.parent / "personas.json"
    if not personas_path.exists():
        print(f"Arquivo {personas_path} não encontrado.")
        raise SystemExit(1)

    with personas_path.open("r", encoding="utf-8") as f:
        personas = json.load(f)

    agente = SimuladorStakeholder()

    for nome, descricao in personas.items():
        print(f"\n{'=' * 70}\nRequisitos para a persona: {nome}\n{'=' * 70}")
        print(agente.gerar_requisitos(descricao))
        time.sleep(5)
