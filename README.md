# 📚 Smart StudyMate — AI-Powered Study Assistant

Smart StudyMate is an AI-powered study assistant that enables students to upload academic PDF documents and ask questions in natural language. It uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant information from uploaded documents and generate context-based answers with source references.

The project runs locally using Ollama, helping reduce dependence on paid cloud APIs.

## ✨ Features

- **PDF Upload:** Upload lecture notes, textbooks, and placement preparation materials.
- **Text Extraction:** Extract text and page information from PDF documents.
- **Document Chunking:** Split long documents into smaller, overlapping text segments.
- **Semantic Search:** Retrieve relevant passages using vector embeddings.
- **AI Question Answering:** Generate answers grounded in retrieved document content.
- **Source References:** Display source filenames, page numbers, and retrieved passages.
- **Local AI Processing:** Use Ollama models without requiring OpenAI API credits.
- **Interactive Interface:** Chat with study materials through a Streamlit web application.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive web interface |
| LangChain | RAG pipeline and document processing |
| PyPDF | PDF text extraction |
| Ollama | Run local language and embedding models |
| ChromaDB | Store and retrieve vector embeddings |
| nomic-embed-text | Generate text embeddings |
| llama3.2:3b | Generate answers using retrieved context |

## 🏗️ System Architecture

```text
        Academic PDF Documents
                  |
                  v
          PDF Text Extraction
                  |
                  v
           Text Chunking
                  |
                  v
          Embedding Generation
           (Ollama Embeddings)
                  |
                  v
             ChromaDB
          Vector Indexing
                  |
                  v
           Student Question
                  |
                  v
          Semantic Retrieval
                  |
                  v
        Relevant Document Chunks
                  |
                  v
         Local LLM (Ollama)
                  |
                  v
       Context-Based Answer
                  |
                  v
       Answer + Source References
```

## 📁 Project Structure

```text
SmartStudyMate/
│
├── app.py
├── rag_pipeline.py
├── config.py
├── requirements.txt
├── README.md
├── .env
├── .gitignore
└── .venv/
```

The `.env` file is optional for the local Ollama configuration and is not required for API authentication.

## ⚙️ Installation and Setup

### 1. Install Python

Install Python 3.10 or 3.11 and verify the installation:

```bash
python --version
```

### 2. Install Ollama

Download and install Ollama from:

https://ollama.com/download

Verify the installation:

```bash
ollama --version
```

### 3. Download the required models

Open a terminal and run:

```bash
ollama pull llama3.2:3b
```

```bash
ollama pull nomic-embed-text
```

The first model generates answers, while the second creates embeddings for semantic search.

### 4. Create a virtual environment

Open the project folder in VS Code and run:

```bash
python -m venv .venv
```

Activate the environment on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install project dependencies

```bash
pip install -r requirements.txt
```

Ensure `langchain-ollama` is included in `requirements.txt`.

### 6. Start Ollama

Ensure the Ollama application is running. If needed, start the service from a terminal:

```bash
ollama serve
```

If Ollama is already running, do not start a second instance.

### 7. Run Smart StudyMate

Execute:

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal, usually:

http://localhost:8501

## 🚀 How to Use

1. Launch Smart StudyMate.
2. Upload one or more text-based PDF documents.
3. Click **Process Documents**.
4. Wait for the text extraction, embedding generation, and indexing to complete.
5. Enter a question about your study materials.
6. Review the generated answer.
7. Expand the source section to inspect the retrieved passages and page references.

## 🧠 How RAG Works

Retrieval-Augmented Generation combines information retrieval with language generation.

1. **Document ingestion:** Extract text from uploaded PDFs.
2. **Chunking:** Divide text into smaller overlapping segments.
3. **Embedding generation:** Convert each segment into a numerical vector.
4. **Vector indexing:** Store vectors and metadata in ChromaDB.
5. **Retrieval:** Find passages relevant to a student's question.
6. **Answer generation:** Supply retrieved evidence to the local LLM.
7. **Source inspection:** Display retrieved passages and their document references.

## 📊 Evaluation

The system should be evaluated using a manually reviewed set of questions and reference answers.

Recommended evaluation metrics:

- **Recall@K:** Measures whether relevant passages appear in the top K retrieved results.
- **Answer Correctness:** Measures agreement with reference answers.
- **Faithfulness:** Measures whether generated claims are supported by retrieved evidence.
- **Abstention Quality:** Measures whether unsupported questions are handled appropriately.
- **Response Latency:** Measures the time required to retrieve evidence and generate answers.

Record actual results before reporting model performance. No benchmark scores are claimed in this repository description.

## ⚠️ Limitations

- Scanned PDFs may require an additional OCR system.
- Answer quality depends on document quality, retrieval relevance, and model capabilities.
- Local inference speed depends on available RAM, CPU, and GPU resources.
- Local models may still generate incorrect or unsupported statements.
- The current implementation stores the vector index in application memory, so documents may need to be processed again after a restart.
- The application is designed as a prototype and has not been independently validated for high-stakes use.

## 🔮 Future Enhancements

- Persistent vector storage and document management.
- Hybrid keyword and semantic retrieval.
- Confidence-aware answer rejection.
- Automatic chapter summaries and revision notes.
- MCQ and quiz generation from uploaded materials.
- Improved handling of scanned PDFs using OCR.
- A systematic evaluation dashboard.
- Deployment with appropriate access controls and resource limits.

## 🔐 Security

- Do not upload API keys, passwords, or private documents to GitHub.
- Keep `.env` and virtual-environment files excluded through `.gitignore`.
- Treat retrieved document text as untrusted input.
- Review privacy and access-control requirements before hosting the application publicly.

## 👨‍💻 Author

**Smart StudyMate** is an academic project demonstrating the application of Generative AI, NLP, semantic search, vector databases, and Retrieval-Augmented Generation to student learning.

## 📄 License

Choose and add an appropriate open-source license before distributing the project publicly.
