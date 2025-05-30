import streamlit as st
from utils.parser import extract_text_from_pdf
from utils.ranker import rank_resumes
import os

st.title("AI-based Resume Ranking App")

job_description = st.text_area("Paste the Job Description:")

uploaded_files = st.file_uploader("Upload Resumes (PDF format)", type=["pdf"], accept_multiple_files=True)

if st.button("Rank Resumes"):
    if not uploaded_files or not job_description:
        st.warning("Please upload resumes and enter a job description.")
    else:
        resumes_text = {file.name: extract_text_from_pdf(file) for file in uploaded_files}
        ranking = rank_resumes(job_description, resumes_text)

        st.subheader("Ranking Results:")
        for i, (name, score) in enumerate(ranking.items(), 1):
            st.write(f"{i}. {name} - Score: {score:.2f}")