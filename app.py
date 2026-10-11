import streamlit as st

from src.ingestion.loader import (
    read_uploaded_file,
)

from src.ingestion.splitter import (
    create_documents,
    split_documents,
)

from src.retrieval.vectorstore import (
    build_vectorstore,
)

from src.rag.qa import (
    ask_rag,
)

from src.graph.workflow import (
    build_career_graph,
)


st.set_page_config(
    page_title="AI Career Copilot",
    page_icon="🤖",
    layout="wide",
)


st.title("🤖 AI Career Copilot")

st.write(
    """
An end-to-end GenAI career assistant built with
LangChain, RAG, ChromaDB, Groq and LangGraph.
"""
)


# --------------------------------------------------
# Session State
# --------------------------------------------------

if "vectorstore" not in st.session_state:

    st.session_state.vectorstore = None


if "chunks" not in st.session_state:

    st.session_state.chunks = []


if "graph_result" not in st.session_state:

    st.session_state.graph_result = None


# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:

    st.header("📄 Upload Documents")

    resume_file = st.file_uploader(
        "Upload Resume",
        type=["pdf", "docx", "txt"],
    )

    jd_file = st.file_uploader(
        "Upload Job Description",
        type=["pdf", "docx", "txt"],
    )

    st.divider()

    build_button = st.button(
        "Build Career Knowledge Base",
        use_container_width=True,
    )


# --------------------------------------------------
# Build RAG Database
# --------------------------------------------------

if build_button:

    if not resume_file or not jd_file:

        st.error(
            "Please upload both resume and job description."
        )

    else:

        with st.spinner(
            "Processing documents..."
        ):

            resume_text = read_uploaded_file(
                resume_file
            )

            jd_text = read_uploaded_file(
                jd_file
            )

            documents = create_documents(
                resume_text,
                jd_text,
            )

            chunks = split_documents(
                documents
            )

            vectorstore = build_vectorstore(
                chunks
            )

            st.session_state.vectorstore = (
                vectorstore
            )

            st.session_state.chunks = chunks

            st.session_state.resume_text = (
                resume_text
            )

            st.session_state.jd_text = (
                jd_text
            )

        st.success(
            f"Knowledge base created with "
            f"{len(chunks)} chunks."
        )


# --------------------------------------------------
# RAG Question Answering
# --------------------------------------------------

st.header("💬 Ask Your Career Documents")


question = st.text_input(
    "Ask a question about your resume and job description",
    placeholder=(
        "Example: What skills am I missing?"
    ),
)


if st.button("Ask"):

    if st.session_state.vectorstore is None:

        st.warning(
            "Build the knowledge base first."
        )

    elif not question:

        st.warning(
            "Please enter a question."
        )

    else:

        with st.spinner(
            "Searching documents and generating answer..."
        ):

            answer, docs = ask_rag(
                st.session_state.vectorstore,
                question,
            )

        st.subheader("Answer")

        st.write(answer)

        with st.expander(
            "Retrieved Sources"
        ):

            for i, doc in enumerate(
                docs,
                start=1
            ):

                st.markdown(
                    f"### Source {i}"
                )

                st.write(
                    doc.page_content
                )

                st.json(
                    doc.metadata
                )


# --------------------------------------------------
# LangGraph Career Analysis
# --------------------------------------------------

st.header("🧠 AI Career Analysis")


analyze_button = st.button(
    "Run Full Career Analysis",
    use_container_width=True,
)


if analyze_button:

    if (
        "resume_text" not in st.session_state
        or "jd_text" not in st.session_state
    ):

        st.warning(
            "Please build the knowledge base first."
        )

    else:

        graph = build_career_graph()

        initial_state = {

            "resume_text":
                st.session_state.resume_text,

            "jd_text":
                st.session_state.jd_text,
        }

        with st.spinner(
            "Running LangGraph workflow..."
        ):

            result = graph.invoke(
                initial_state
            )

        st.session_state.graph_result = result


# --------------------------------------------------
# Display LangGraph Result
# --------------------------------------------------

if st.session_state.graph_result:

    result = (
        st.session_state.graph_result
    )

    st.subheader(
        "📊 Career Analysis"
    )

    st.write(
        f"**Risk Level:** "
        f"{result.get('risk_level', 'N/A')}"
    )

    with st.expander(
        "Resume Analysis"
    ):

        st.write(
            result.get(
                "resume_analysis",
                ""
            )
        )

    with st.expander(
        "Job Description Analysis"
    ):

        st.write(
            result.get(
                "jd_analysis",
                ""
            )
        )

    with st.expander(
        "Gap Analysis"
    ):

        st.write(
            result.get(
                "gap_analysis",
                ""
            )
        )

    if result.get("improvement"):

        with st.expander(
            "Improvement Plan"
        ):

            st.write(
                result["improvement"]
            )

    st.subheader(
        "📋 Final Career Report"
    )

    st.write(
        result.get(
            "final_report",
            ""
        )
    )