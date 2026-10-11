import shutil
from pathlib import Path
from typing import List
from langchain_chroma import Chroma
from langchain_core.documents import Document
from src.config import CHROMA_DIR
from src.ingestion.embeddings import get_embeddings

COLLECTION_NAME = "career_copilot"

def build_vectorstore(chunks: List[Document],):
        if Path(CHROMA_DIR).exists():
              shutil.rmtree(CHROMA_DIR)
    
        vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=get_embeddings(),
        persist_directory=str(CHROMA_DIR),
        collection_name=COLLECTION_NAME,
         )

        return vectorstore