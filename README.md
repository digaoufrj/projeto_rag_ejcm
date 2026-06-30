# Sistema RAG - EJCM

Módulo de Retrieval (Busca Vetorial) para sistema RAG usando ChromaDB e Google Gemini Embeddings.

## 📋 Requisitos

- Python 3.10+
- Conta Google AI Studio (para API key)

## 🚀 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/SEU_USUARIO/projeto_rag_ejcm.git
cd projeto_rag_ejcm
```

2. Crie e ative o ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure a API key:
```bash
cp .env.example .env
# Edite o arquivo .env e adicione sua GOOGLE_API_KEY
```

Obtenha sua chave em: https://aistudio.google.com/app/apikey

## 📁 Estrutura do Projeto

```
projeto_rag_ejcm/
├── base_conhecimento_ejcm/        # PDFs e TXTs da base de conhecimento
├── chroma_db/                     # Banco vetorial (gerado automaticamente)
├── agents/                        # Agentes LLM do pipeline
│   ├── __init__.py
│   ├── simulador.py               # Simulador de Stakeholders
│   └── consolidador.py            # Consolidador de Requisitos
├── personas.json                  # Descrições das personas (stakeholders)
├── rag_retriever.py               # Módulo de Retrieval (RAG)
├── main.py                        # Orquestrador do pipeline completo
├── requirements.txt               # Dependências Python
├── .env                           # Variáveis de ambiente (NÃO commitar)
└── .env.example                   # Template de configuração
```

## 🔄 Fluxo do Sistema

```
    [personas.json]
          ↓
    [Simulador] x N personas → requisitos individuais por persona
          ↓
    [Consolidador] ← contexto do RAG (base de conhecimento da EJCM)
          ↓
    requisitos_consolidados.md
```

1. **Simulador** roda uma vez por persona, gerando requisitos individuais
2. Todos os requisitos são unificados pelo **Consolidador**, que também consulta a base de conhecimento via RAG
3. Saída final: documento único em Markdown

## ▶️ Executar Pipeline Completo

```bash
python main.py
```

**Arquivos gerados:**
- `requisitos_individuais.json` — requisitos por persona (auditoria)
- `requisitos_consolidados.md` — documento final unificado

## 🧪 Testar Módulos Individualmente

```bash
# Apenas o RAG
python rag_retriever.py

# Apenas o Simulador (roda para todas as personas)
python -m agents.simulador

# Apenas o Consolidador (com requisitos mock)
python -m agents.consolidador
```

## 💻 Uso

### Teste standalone

```bash
python rag_retriever.py
```

### Integração no seu código

```python
from rag_retriever import buscar_contexto_ejcm

# Busca os 3 trechos mais relevantes
contexto = buscar_contexto_ejcm("Qual o horário de funcionamento?", top_k=3)
print(contexto)
```

## 📝 Adicionando Documentos

1. Coloque arquivos `.pdf` ou `.txt` na pasta `base_conhecimento_ejcm/`
2. Delete a pasta `chroma_db/` (se existir)
3. Execute `python rag_retriever.py` para reindexar

## 🔧 Configurações

Edite as constantes em `rag_retriever.py`:

- `CHUNK_SIZE`: Tamanho dos chunks (padrão: 1000)
- `CHUNK_OVERLAP`: Sobreposição entre chunks (padrão: 200)
- `MODELO_EMBEDDING`: Modelo de embeddings (padrão: `models/gemini-embedding-001`)

## 📦 Dependências Principais

- `langchain` - Framework para LLMs
- `langchain-google-genai` - Integração com Google Gemini
- `chromadb` - Banco de dados vetorial
- `pypdf` - Leitura de PDFs
- `python-dotenv` - Gerenciamento de variáveis de ambiente

## ⚠️ Segurança

- **NUNCA** commite o arquivo `.env` com sua API key
- O `.gitignore` já está configurado para proteger arquivos sensíveis
- Revogue chaves expostas imediatamente em: https://aistudio.google.com/app/apikey

## 📄 Licença

MIT
