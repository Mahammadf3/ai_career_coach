from langchain_core.output_parsers import StrOutputParser

from src.llm import get_llm
from src.prompts import (
    RESUME_ANALYSIS_PROMPT,
    JD_ANALYSIS_PROMPT,
    GAP_ANALYSIS_PROMPT,
    RISK_PROMPT,
    FINAL_REPORT_PROMPT,
)


def resume_analysis_node(state):

    llm = get_llm(
        temperature=0.2
    )

    chain = (
        RESUME_ANALYSIS_PROMPT
        | llm
        | StrOutputParser()
    )

    result = chain.invoke(
        {
            "resume": state["resume_text"]
        }
    )

    return {
        "resume_analysis": result
    }


def jd_analysis_node(state):

    llm = get_llm(
        temperature=0.2
    )

    chain = (
        JD_ANALYSIS_PROMPT
        | llm
        | StrOutputParser()
    )

    result = chain.invoke(
        {
            "job_description": state["jd_text"]
        }
    )

    return {
        "jd_analysis": result
    }


def gap_analysis_node(state):

    llm = get_llm(
        temperature=0.2
    )

    chain = (
        GAP_ANALYSIS_PROMPT
        | llm
        | StrOutputParser()
    )

    result = chain.invoke(
        {
            "resume_analysis":
                state["resume_analysis"],

            "jd_analysis":
                state["jd_analysis"],
        }
    )

    return {
        "gap_analysis": result
    }


def risk_level_node(state):

    llm = get_llm(
        temperature=0.0
    )

    chain = (
        RISK_PROMPT
        | llm
        | StrOutputParser()
    )

    result = chain.invoke(
        {
            "gap_analysis":
                state["gap_analysis"]
        }
    )

    risk = result.strip().upper()

    if "HIGH" in risk:
        risk = "HIGH"

    elif "MEDIUM" in risk:
        risk = "MEDIUM"

    else:
        risk = "LOW"

    return {
        "risk_level": risk
    }


def improvement_node(state):

    llm = get_llm(
        temperature=0.3
    )

    prompt = f"""
You are an expert AI career coach.

The candidate has HIGH career-fit risk.

Gap analysis:

{state["gap_analysis"]}

Create a practical improvement plan.

Include:

1. Missing skills
2. What to learn first
3. Projects to build
4. Interview preparation
5. Resume improvements
"""

    result = llm.invoke(prompt)

    return {
        "improvement": result.content
    }


def final_report_node(state):

    llm = get_llm(
        temperature=0.2
    )

    chain = (
        FINAL_REPORT_PROMPT
        | llm
        | StrOutputParser()
    )

    result = chain.invoke(
        {
            "resume_analysis":
                state["resume_analysis"],

            "jd_analysis":
                state["jd_analysis"],

            "gap_analysis":
                state["gap_analysis"],

            "risk_level":
                state["risk_level"],
        }
    )

    return {
        "final_report": result
    }