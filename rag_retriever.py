"""
rag_retriever.py
----------------
Módulo de Retrieval (Busca Vetorial) do sistema RAG da EJCM.

Responsabilidades:
    * Carregar e fatiar documentos (PDF/TXT) da base de conhecimento.
    * Gerar / persistir embeddings em um ChromaDB local
      (modelo `models/text-embedding-004` via Google Generative AI).
    * Expor `buscar_contexto_ejcm(query, top_k)` para o Agente Gerador (LLM).

Este módulo NÃO instancia nenhum modelo de geração de texto.
Apenas pipeline de embeddings + busca vetorial.

Requisitos:
    Python 3.10+
    langchain, langchain-community, langchain-google-genai, chromadb, pypdf
"""

from __future__ import annotations

import logging
import os
from pathlib import Path
from typing import List

from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

# ---------------------------------------------------------------------------
# Configurações globais
# ---------------------------------------------------------------------------

BASE_DIR: Path = Path(__file__).parent.resolve()
DIRETORIO_DOCUMENTOS: Path = BASE_DIR / "base_conhecimento_ejcm"
DIRETORIO_CHROMA: Path = BASE_DIR / "chroma_db"

NOME_COLECAO: str = "base_ejcm"
MODELO_EMBEDDING: str = "models/gemini-embedding-001"

CHUNK_SIZE: int = 1000
CHUNK_OVERLAP: int = 200

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s - %(name)s - %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("rag_retriever")


# ---------------------------------------------------------------------------
# Carregamento e Chunking
# ---------------------------------------------------------------------------

def carregar_e_fatiar_documentos(
    diretorio: Path = DIRETORIO_DOCUMENTOS,
) -> List[Document]:
    """Lê todos os PDFs e TXTs do diretório informado e os divide em chunks.

    Utiliza `RecursiveCharacterTextSplitter` com `chunk_size=1000`
    e `chunk_overlap=200`. Adiciona o nome do arquivo de origem nos
    metadados de cada chunk (chave `source`).

    Args:
        diretorio: Pasta onde estão os documentos da base de conhecimento.

    Returns:
        Lista de `Document` já fatiados, prontos para vetorização.
    """
    if not diretorio.exists():
        logger.warning("Diretório de documentos inexistente: %s", diretorio)
        return []

    documentos: List[Document] = []

    for caminho in sorted(diretorio.iterdir()):
        if not caminho.is_file():
            continue

        sufixo = caminho.suffix.lower()
        try:
            if sufixo == ".pdf":
                loader = PyPDFLoader(str(caminho))
            elif sufixo == ".txt":
                loader = TextLoader(str(caminho), encoding="utf-8")
            else:
                logger.debug("Ignorando arquivo não suportado: %s", caminho.name)
                continue

            carregados = loader.load()
            for doc in carregados:
                doc.metadata["source"] = caminho.name
            documentos.extend(carregados)
            logger.info("Carregado: %s (%d página(s)/bloco(s))",
                        caminho.name, len(carregados))
        except Exception as exc:  # noqa: BLE001
            logger.error("Falha ao carregar %s: %s", caminho.name, exc)

    if not documentos:
        logger.warning("Nenhum documento válido encontrado em %s", diretorio)
        return []

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=["\n\n", "\n", ". ", " ", ""],
    )
    chunks = splitter.split_documents(documentos)
    logger.info("Total de chunks gerados: %d", len(chunks))
    return chunks


# ---------------------------------------------------------------------------
# Inicialização do Banco Vetorial
# ---------------------------------------------------------------------------

def _get_embeddings() -> GoogleGenerativeAIEmbeddings:
    """Instancia o modelo de embeddings do Google.

    Requer a variável de ambiente `GOOGLE_API_KEY`.

    Raises:
        EnvironmentError: Se a chave da API não estiver definida.
    """
    if not os.getenv("GOOGLE_API_KEY"):
        raise EnvironmentError(
            "Variável de ambiente GOOGLE_API_KEY não definida. "
            "Configure-a antes de executar o módulo."
        )
    return GoogleGenerativeAIEmbeddings(model=MODELO_EMBEDDING)


def inicializar_banco_vetorial(
    diretorio_persistencia: Path = DIRETORIO_CHROMA,
    diretorio_documentos: Path = DIRETORIO_DOCUMENTOS,
) -> Chroma:
    """Inicializa (ou carrega) o ChromaDB persistido em disco.

    Se já existir um banco em `diretorio_persistencia`, ele é apenas carregado
    — evitando gerar embeddings novamente. Caso contrário, lê os documentos,
    gera os embeddings e persiste o índice.

    Args:
        diretorio_persistencia: Pasta onde o ChromaDB é/será gravado.
        diretorio_documentos: Pasta com os arquivos-fonte (PDF/TXT).

    Returns:
        Instância de `Chroma` pronta para uso.
    """
    embeddings = _get_embeddings()
    diretorio_persistencia.mkdir(parents=True, exist_ok=True)

    banco_existente = any(diretorio_persistencia.iterdir())

    if banco_existente:
        logger.info("Banco vetorial existente encontrado. Carregando de %s ...",
                    diretorio_persistencia)
        return Chroma(
            collection_name=NOME_COLECAO,
            embedding_function=embeddings,
            persist_directory=str(diretorio_persistencia),
        )

    logger.info("Nenhum banco vetorial encontrado. Construindo do zero...")
    chunks = carregar_e_fatiar_documentos(diretorio_documentos)
    if not chunks:
        logger.warning(
            "Criando ChromaDB vazio — adicione documentos em %s e re-execute.",
            diretorio_documentos,
        )
        return Chroma(
            collection_name=NOME_COLECAO,
            embedding_function=embeddings,
            persist_directory=str(diretorio_persistencia),
        )

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        collection_name=NOME_COLECAO,
        persist_directory=str(diretorio_persistencia),
    )
    logger.info("Banco vetorial construído e persistido em %s",
                diretorio_persistencia)
    return vectordb


# ---------------------------------------------------------------------------
# Função pública de busca
# ---------------------------------------------------------------------------

def buscar_contexto_ejcm(query: str, top_k: int = 3) -> str:
    """Busca no banco vetorial os `top_k` trechos mais relevantes para `query`.

    Retorna uma string única, formatada, com os trechos separados e
    indicando a fonte (nome do arquivo). Em caso de erro, registra um log
    e retorna string vazia — garantindo que o Agente Gerador não quebre.

    Args:
        query: Pergunta/consulta em linguagem natural.
        top_k: Quantidade de trechos a recuperar (padrão = 3).

    Returns:
        Contexto formatado pronto para ser injetado no prompt do LLM,
        ou string vazia em caso de falha.
    """
    if not query or not query.strip():
        logger.warning("Query vazia recebida em buscar_contexto_ejcm.")
        return ""

    try:
        vectordb = inicializar_banco_vetorial()
        resultados: List[Document] = vectordb.similarity_search(query, k=top_k)

        if not resultados:
            logger.info("Nenhum resultado retornado para a query: %r", query)
            return ""

        blocos: List[str] = []
        for i, doc in enumerate(resultados, start=1):
            fonte = doc.metadata.get("source", "desconhecida")
            pagina = doc.metadata.get("page")
            cabecalho = f"[Trecho {i} | Fonte: {fonte}"
            if pagina is not None:
                cabecalho += f" | Página: {pagina}"
            cabecalho += "]"
            blocos.append(f"{cabecalho}\n{doc.page_content.strip()}")

        return "\n\n---\n\n".join(blocos)

    except Exception as exc:  # noqa: BLE001
        logger.error("Erro durante a busca de contexto: %s", exc, exc_info=True)
        return ""


# ---------------------------------------------------------------------------
# Bloco de teste
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    DIRETORIO_DOCUMENTOS.mkdir(parents=True, exist_ok=True)

    print("=" * 70)
    print(" Teste do módulo de Retrieval - EJCM RAG ")
    print("=" * 70)
    print(f"Pasta de documentos: {DIRETORIO_DOCUMENTOS}")
    print(f"Pasta do ChromaDB : {DIRETORIO_CHROMA}")
    print()
    print(">> Coloque arquivos .pdf ou .txt em "
          f"'{DIRETORIO_DOCUMENTOS.name}/' antes de rodar a primeira vez.")
    print(">> Certifique-se de ter exportado GOOGLE_API_KEY no ambiente.")
    print()

    query_teste = "O que é a EJCM e quais serviços ela oferece?"
    print(f"Consulta de teste: {query_teste!r}\n")

    contexto = buscar_contexto_ejcm(query_teste, top_k=3)

    print("-" * 70)
    if contexto:
        print("Contexto recuperado:\n")
        print(contexto)
    else:
        print("Nenhum contexto retornado (verifique documentos, API key e logs).")
    print("-" * 70)
