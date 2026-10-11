from langchain_core.prompts import ChatPromptTemplate


RAG_PROMPT = ChatPromptTemplate.from_template(
    """
You are an expert AI career coach.

Use ONLY the provided context to answer the question.

If the answer cannot be found in the context,
clearly say that the information is not available.

Context:
{context}

Question:
{question}

Provide a clear and practical answer.
"""
)


RESUME_ANALYSIS_PROMPT = ChatPromptTemplate.from_template(
    """
You are an expert technical recruiter.

Analyze the following resume.

Resume:
{resume}

Identify:

1. Technical skills
2. Programming languages
3. AI/ML skills
4. GenAI skills
5. Projects
6. Experience
7. Strengths
8. Missing information

Return a structured professional analysis.
"""
)


JD_ANALYSIS_PROMPT = ChatPromptTemplate.from_template(
    """
You are an expert technical recruiter.

Analyze the following job description.

Job Description:
{job_description}

Identify:

1. Required technical skills
2. Required programming languages
3. AI/ML requirements
4. GenAI requirements
5. Experience requirements
6. Important responsibilities
7. Nice-to-have skills

Return a structured professional analysis.
"""
)


GAP_ANALYSIS_PROMPT = ChatPromptTemplate.from_template(
    """
You are an AI career advisor.

Compare the resume information with the job description.

RESUME:
{resume_analysis}

JOB DESCRIPTION:
{jd_analysis}

Identify:

1. Matching skills
2. Missing skills
3. Partially matching skills
4. Experience gaps
5. Project gaps
6. Recommended learning priorities

Give a practical analysis.
"""
)


RISK_PROMPT = ChatPromptTemplate.from_template(
    """
Based on the following career gap analysis:

{gap_analysis}

Classify the candidate's overall job-fit risk.

Return ONLY ONE of:

LOW
MEDIUM
HIGH
"""
)


FINAL_REPORT_PROMPT = ChatPromptTemplate.from_template(
    """
You are an expert AI career coach.

Create a professional career assessment using:

Resume Analysis:
{resume_analysis}

Job Description Analysis:
{jd_analysis}

Gap Analysis:
{gap_analysis}

Risk Level:
{risk_level}

Create the following sections:

1. Overall Assessment
2. Matching Skills
3. Missing Skills
4. Priority Learning Areas
5. Resume Improvement Suggestions
6. Interview Preparation Suggestions
7. Final Recommendation

Be specific and practical.
"""
)