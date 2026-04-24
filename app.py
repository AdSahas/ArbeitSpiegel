import streamlit as st

from backend.llm import call_llm
from backend.prompts import cv_prompt, coverLetter_prompt, skillGap_analysis


def analyse(cv: str, job: str):
    cv_result = call_llm(cv_prompt(cv, job))
    cover_letter_result = call_llm(coverLetter_prompt(cv, job))
    skill_gap_result = call_llm(skillGap_analysis(cv, job))

    return {
        "cv_analysis": cv_result,
        "cover_letter": cover_letter_result,
        "skill_gap_analysis": skill_gap_result,
    }


st.set_page_config(page_title="ArbeitSpiegel", page_icon="🧠", layout="wide")

st.title("🧠 ArbeitSpiegel")
st.write("AI Job Application Copilot")

cv = st.text_area("Paste your CV", height=300)
job = st.text_area("Paste the Job Description", height=300)

if st.button("Analyze Application"):
    if not cv.strip() or not job.strip():
        st.warning("Please paste both a CV and a job description.")
    else:
        with st.spinner("Analyzing your application..."):
            result = analyse(cv, job)

        st.subheader("CV Analysis and Rewritten CV")
        st.text_area(
            "CV Analysis Output",
            value=result["cv_analysis"],
            height=500,
        )

        st.subheader("Cover Letter")
        st.text_area(
            "Cover Letter Output",
            value=result["cover_letter"],
            height=350,
        )

        st.subheader("Skill Gap Analysis")
        st.text_area(
            "Skill Gap Output",
            value=result["skill_gap_analysis"],
            height=350,
        )
