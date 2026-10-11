from langchain_groq import ChatGroq

from src.config import GROQ_API_KEY, MODEL_NAME


def get_llm(
    temperature: float = 0.2,
):
    """
    Create and return the Groq chat model.
    """

    return ChatGroq(
        model=MODEL_NAME,
        temperature=temperature,
        api_key=GROQ_API_KEY,
    )