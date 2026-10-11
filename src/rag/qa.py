from typing import List, Tuple

from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser

from src.llm import get_llm
from src.prompts import RAG_PROMPT


def retrieve_context(vectorstore,query: str,k: int = 5,) -> Tuple[str, List[Document]]:
    retriever = vectorstore.as_retriever(
        search_kwargs={
            "k": k
        }
    )

    docs = retriever.invoke(query)

    context = "\n\n".join(
        [
            (
                f"SOURCE: {doc.metadata}\n"
                f"CONTENT:\n{doc.page_content}"
            )
            for doc in docs
        ]
    )

    return context, docs


def ask_rag(vectorstore,question: str,):

    context, docs = retrieve_context(
        vectorstore,
        question,
    )

    llm = get_llm(
        temperature=0.2
    )

    chain = (
        RAG_PROMPT
        | llm
        | StrOutputParser()
    )

    answer = chain.invoke(
        {
            "context": context,
            "question": question,
        }
    )

    return answer, docs