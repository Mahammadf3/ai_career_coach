# AI Career Copilot — GenAI, RAG & LangGraph

An AI-powered career assistant that analyzes resumes against job descriptions, identifies skill gaps, retrieves relevant document context using Retrieval-Augmented Generation (RAG), and generates personalized career improvement recommendations.

Built using Python, LangChain, Groq, Hugging Face embeddings, ChromaDB, LangGraph, and Streamlit.

## 1. Project Overview

AI Career Copilot helps candidates understand how their resumes align with a target job description.

Users upload their resume and a job description. The application extracts the text, splits documents into chunks, generates embeddings, and stores them in ChromaDB.

The application provides two main capabilities:

- **RAG Question Answering:** Ask questions about uploaded career documents and receive answers based on retrieved document context.
- **LangGraph Career Analysis:** Analyze the resume and job description, identify skill gaps, classify job-fit risk, generate improvement recommendations, and produce a final career report.

## 2. Key Features

- Upload resumes and job descriptions in PDF, DOCX, or TXT format.
- Extract and preprocess document text.
- Split documents into manageable chunks with overlapping context.
- Generate embeddings using Hugging Face sentence-transformer models.
- Store and retrieve document embeddings using ChromaDB.
- Answer questions using Retrieval-Augmented Generation.
- Use LangChain prompt templates and LLM chains.
- Analyze resumes and job descriptions independently.
- Identify matching skills, missing skills, and experience gaps.
- Classify job-fit risk as LOW, MEDIUM, or HIGH.
- Generate personalized career improvement plans.
- Orchestrate multi-step workflows using LangGraph.
- Display results through an interactive Streamlit interface.

## 3. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application frontend |
| LangChain | LLM integration and RAG pipeline |
| Groq | Hosted LLM inference |
| Hugging Face | Text embedding model |
| ChromaDB | Vector database |
| LangGraph | Stateful, multi-step workflow orchestration |
| PyPDF | PDF text extraction |
| docx2txt | DOCX text extraction |
| python-dotenv | Environment variable management |

## 4. Application Architecture

```text
                  Streamlit UI
                       |
             Upload Resume + Job Description
                       |
                 Document Loader
                       |
                  Text Extraction
                       |
                  Text Splitter
                       |
                    Chunks
                       |
                    Embeddings
                       |
                    ChromaDB
                       |
                RAG Question Answering
                       |
                Retriever + Context
                       |
                    Groq LLM
                       |
                   RAG Answer
```

The career analysis workflow uses LangGraph:

```text
          Initial CareerState
                   |
                   v
          Resume Analysis
                   |
                   v
       Job Description Analysis
                   |
                   v
             Gap Analysis
                   |
                   v
            Risk Assessment
                   |
             Conditional Router
               /         \
            HIGH       LOW/MEDIUM
              |            |
              v            |
       Improvement Plan    |
              |            |
              +-----+------+
                    |
                    v
              Final Report
                    |
                    v
                   END
```

## 5. Project Folder Structure

```text
ai-career-copilot/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
│
├── data/
│   ├── uploads/
│   └── chroma/
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── state.py
│   ├── llm.py
│   ├── prompts.py
│   │
│   ├── ingestion/
│   │   ├── __init__.py
│   │   ├── loader.py
│   │   ├── splitter.py
│   │   └── embeddings.py
│   │
│   ├── retrieval/
│   │   ├── __init__.py
│   │   └── vectorstore.py
│   │
│   ├── rag/
│   │   ├── __init__.py
│   │   └── qa.py
│   │
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── nodes.py
│   │   └── router.py
│   │
│   ├── graph/
│   │   ├── __init__.py
│   │   └── workflow.py
```

### Main module responsibilities

- `app.py`: Streamlit interface and application flow.
- `config.py`: Model names, API configuration, directories, and RAG settings.
- `llm.py`: Initializes the Groq chat model.
- `prompts.py`: Stores reusable prompt templates.
- `loader.py`: Extracts text from uploaded documents.
- `splitter.py`: Splits documents into overlapping chunks.
- `embeddings.py`: Initializes the embedding model.
- `vectorstore.py`: Creates and manages the ChromaDB vector store.
- `qa.py`: Retrieves relevant chunks and generates RAG answers.
- `state.py`: Defines the LangGraph `CareerState`.
- `nodes.py`: Implements resume analysis, job analysis, gap analysis, risk assessment, and report generation.
- `router.py`: Implements conditional routing.
- `workflow.py`: Defines and compiles the LangGraph workflow.
- `tests/`: Contains automated tests for core functionality.

## 6. Prerequisites

Before running the project, install:

- Python 3.10 or a compatible Python version supported by the selected dependencies.
- Git (optional, for version control).
- A Groq API key.
- An internet connection for Groq API requests and initial embedding-model downloads.

## 7. Installation and Setup

### Step 1: Clone the repository

```bash
git clone <your-repository-url>
cd ai-career-copilot
```

If you have not created a GitHub repository, create the project directory locally instead.

### Step 2: Create a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### Step 3: Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Step 4: Configure environment variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

Replace the placeholder with your actual API key.

Never commit `.env` or expose your API key in source code.

### Step 5: Verify the project structure

Make sure the required Python modules and package `__init__.py` files exist.

## 8. Run the Application

From the project root, with the virtual environment activated:

```bash
streamlit run app.py
```

Streamlit will display a local URL in the terminal. Open that URL in your browser.

### How to use the application

1. Upload your resume.
2. Upload the target job description.
3. Select **Build Career Knowledge Base**.
4. Ask questions about the documents in the RAG question-answering section.
5. Select **Run Full Career Analysis**.
6. Review the resume analysis, job-description analysis, skill-gap analysis, risk level, improvement plan, and final report.

## 9. How RAG Works

Retrieval-Augmented Generation combines document retrieval with LLM generation.

1. Extract text from the uploaded documents.
2. Split the text into chunks.
3. Convert the chunks into embedding vectors.
4. Store the vectors in ChromaDB.
5. Convert the user's question into a retrieval query.
6. Retrieve the most relevant chunks.
7. Insert the retrieved context into a prompt.
8. Send the prompt to the Groq LLM.
9. Return the generated answer and retrieved sources.

The answer depends on the quality of the uploaded documents and the relevance of the retrieved context.

## 10. How LangGraph Works

LangGraph coordinates the career analysis as a stateful workflow.

The `CareerState` TypedDict defines the fields that travel through the graph.

The initial state contains the resume text and job description text:

```python
initial_state = {
    "resume_text": resume_text,
    "jd_text": jd_text,
}
```

The graph is executed with:

```python
result = graph.invoke(initial_state)
```

Each node reads the current state and returns updates, such as `resume_analysis`, `gap_analysis`, or `risk_level`.

A conditional router selects the next node based on the risk classification.

This design separates workflow orchestration from individual analysis tasks and makes the application easier to maintain and extend.

## 11. Configuration

The application uses configurable values for:

- Groq model name.
- Hugging Face embedding model.
- Chunk size.
- Chunk overlap.
- Number of retrieved chunks (`top_k`).
- ChromaDB persistence directory.

Adjust these settings in `src/config.py` as required.

## 12. Testing

Run automated tests from the project root:

```bash
pytest -q
```

The tests should cover document loading, text splitting, and retrieval behavior.

Test files must be implemented before this command can validate the corresponding functionality.

## 13. Security and Limitations

- Keep API keys in environment variables.
- Do not commit resumes, job descriptions, or private candidate data to Git.
- Treat uploaded documents as untrusted input.
- Validate file types and impose upload-size limits.
- Avoid interpreting LLM-generated risk levels as objective hiring decisions.
- Verify generated career recommendations before acting on them.
- Scanned PDFs may require OCR, which is not included in the current implementation.
- The application sends prompts and relevant document content to the configured hosted LLM provider.
- Local ChromaDB persistence is not equivalent to a production-grade, multi-user database.

## 14. Skills Demonstrated

This project demonstrates practical experience with:

- Python application development.
- Environment and dependency management.
- LLM API integration.
- Prompt engineering.
- Document processing and chunking.
- Embeddings and vector databases.
- Semantic retrieval.
- Retrieval-Augmented Generation.
- LangChain chains and output parsers.
- Streamlit application development.
- TypedDict-based state definition.
- LangGraph nodes, edges, and conditional routing.
- Multi-step AI workflow orchestration.
- Basic automated testing and error handling.

## 15. Future Enhancements Within the Current Learning Scope

- Add human approval before final report generation.
- Add validation and error handling for malformed documents.
- Improve retrieval quality with metadata filtering.
- Add evaluation examples for retrieval and answer quality.
- Add report export functionality.
- Improve the interface with workflow status indicators.

## 16. Author

**AI Career Copilot — GenAI Portfolio Project**

Built as a hands-on project to demonstrate the integration of LLMs, RAG, LangChain, vector databases, Streamlit, and LangGraph in a practical application.
