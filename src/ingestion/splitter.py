from typing import List, Tuple
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.config import CHUNK_SIZE, CHUNK_OVERLAP

def create_documents(resume_text: str,jd_text: str,) -> List[Document]:
     return [
        Document(
            page_content=resume_text,
            metadata={
                "source": "uploaded_resume",
                "doc_type": "resume",
            },
        ),
        Document(
            page_content=jd_text,
            metadata={
                "source": "uploaded_job_description",
                "doc_type": "job_description",
            },
        ),
    ]

def split_documents(documents: List[Document],) -> List[Document]:

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=[
            "\n\n",
            "\n",
            ".",
            " ",
            "",
        ],
    )

    return splitter.split_documents(documents)