"""
agents/consolidador.py
----------------------
Agente Consolidador de Requisitos.

Recebe requisitos gerados por múltiplas personas/stakeholders e produz
um documento final unificado, usando o contexto da Base de Conhecimento
(via RAG) para validar e contextualizar.

Autoria original: Giovanna / Cássio (adaptado para integrar ao projeto).
"""

from __future__ import annotations

import logging
import os
from typing import Optional

from dotenv import load_dotenv
from google import genai
from google.genai import types

from rag_retriever import buscar_contexto_ejcm

load_dotenv()

logger = logging.getLogger("agente_consolidador")


class ConsolidadorRequisitos:
    """Agente LLM responsável por consolidar requisitos de múltiplas personas.

    Usa o modelo Gemini para analisar, comparar, reconciliar e consolidar
    os requisitos recebidos, apoiando-se no contexto vindo do RAG.
    """

    PROMPT_SISTEMA = """
Você é um Especialista em Engenharia de Requisitos responsável pela consolidação de requisitos provenientes de múltiplos stakeholders simulados.
Sua função é analisar, comparar, reconciliar e consolidar os requisitos recebidos, produzindo um documento final coerente, consistente e alinhado ao domínio do sistema.
Você possui acesso a uma Base de Conhecimento composta por documentos institucionais, normativos e registros de processos existentes. Utilize essas informações para validar, complementar e contextualizar os requisitos sempre que necessário.

Instruções:

- Analise atentamente o contexto fornecido e identifique os requisitos principais para o domínio especificado, unificando as diferentes visões dos stakeholders.
- Compare os requisitos e identifique requisitos conflitantes, ambíguos ou redundantes. Resolva-os de forma que melhor se adequem ao sistema.
- Gere requisitos claros, consistentes, não genéricos e não ambíguos.

Saída esperada:
- Lista final de requisitos funcionais e requisitos não funcionais
"""

    def __init__(
        self,
        model: str = "gemini-3.5-flash",
        temperature: float = 0.4,
        api_key: Optional[str] = None,
    ) -> None:
        """Inicializa o agente consolidador.

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

    def consolidar(
        self,
        requisitos_por_persona: dict,
        dominio_sistema: Optional[str] = None,
        query_rag: Optional[str] = None,
        top_k: int = 5,
    ) -> str:
        """Consolida os requisitos das personas em um documento final.

        Args:
            requisitos_por_persona: Dicionário `{nome_persona: requisitos}`.
            dominio_sistema: Contexto/domínio do sistema. Se None e `query_rag`
                for informada, busca automaticamente via RAG.
            query_rag: Consulta para o RAG buscar contexto na base de
                conhecimento. Ignorada se `dominio_sistema` for fornecido.
            top_k: Quantidade de trechos a recuperar do RAG (padrão = 5).

        Returns:
            Texto consolidado com a lista final de requisitos, ou mensagem
            de erro em caso de falha.
        """
        if dominio_sistema is None:
            if query_rag:
                logger.info("Buscando contexto no RAG com query: %r", query_rag)
                dominio_sistema = buscar_contexto_ejcm(query_rag, top_k=top_k)
            else:
                dominio_sistema = ""

        config = types.GenerateContentConfig(
            system_instruction=self.PROMPT_SISTEMA,
            temperature=self.temperature,
        )

        prompt_usuario = (
            f"## Domínio do Sistema (Base de Conhecimento)\n{dominio_sistema}\n\n"
        )
        for nome_persona, requisitos in requisitos_por_persona.items():
            prompt_usuario += (
                f"### Requisitos gerados por: {nome_persona}\n{requisitos}\n\n"
            )

        try:
            resposta = self.client.models.generate_content(
                model=self.model,
                contents=prompt_usuario,
                config=config,
            )
            return resposta.text
        except Exception as exc:  # noqa: BLE001
            logger.error("Falha na consolidação: %s", exc, exc_info=True)
            return f"Erro: {exc}"


if __name__ == "__main__":
    # ---- Teste rápido ----
    logging.basicConfig(level=logging.INFO)

    # Requisitos virão de outros agentes (ainda em desenvolvimento).
    # Por enquanto, mock para validar a integração.
    requisitos_mock = {
        "Gerente da Padaria": (
            "1. O sistema deve controlar o estoque de pães.\n"
            "2. Necessário relatório diário de vendas."
        ),
        "Cliente": (
            "1. Quero ver os horários de funcionamento online.\n"
            "2. Precisa ter opção de reservar pão de queijo."
        ),
    }

    agente = ConsolidadorRequisitos(model="gemini-3.5-flash")

    documento_final = agente.consolidar(
        requisitos_por_persona=requisitos_mock,
        query_rag="regulamento e processos da padaria",
        top_k=3,
    )

    print("=" * 70)
    print(" DOCUMENTO FINAL CONSOLIDADO ")
    print("=" * 70)
    print(documento_final)
