# streamlit app for frontend.
import requests
import streamlit as st

st.title("ArbeitSpiegel - AI CV Optimizer and Career Coach")
st.write("Upload your CV and a job description to get personalized feedback and advice.")

cv = st.text_area("Paste your CV here:")
job = st.text_area("Paste the job description here:")

if st.button("Analyse"):
    try:
        response = requests.post("http://localhost:8000/analyse",
                                 json={
                                     "cv": cv,
                                       "job": job
                                       }
                                    )
        result = response.json()

        st.subheader("CV Analysis and Rewritten CV")
        st.write(result["cv_analysis"])

        st.subheader("Cover Letter")
        st.write(result["cover_letter"])

        st.subheader("Skill Gap Analysis")
        st.write(result["skill_gap_analysis"])

    except Exception as e:
        st.error(f"Error occurred: {e}")
