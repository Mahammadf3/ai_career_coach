from typing import List, TypedDict


class CareerState(TypedDict, total=False):

    resume_text: str

    jd_text: str

    resume_analysis: str

    jd_analysis: str

    retrieved_context: str

    gap_analysis: str

    risk_level: str

    improvement: str

    final_report: str

    human_approved: bool

    messages: List[str]