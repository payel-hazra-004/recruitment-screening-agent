import streamlit as st
import PyPDF2

st.set_page_config(page_title="Recruitment Screening Agent")
st.title("📄 Recruitment Screening Agent")
st.write("Upload a Job Description and Resume to begin.")

uploaded_jd = st.file_uploader("Upload Job Description (TXT)", type=["txt"])
uploaded_resume = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

jd_text = ""
resume_text = ""

if uploaded_jd is not None:
    jd_text = uploaded_jd.read().decode("utf-8")
    st.success("Job Description uploaded successfully!")

if uploaded_resume is not None:
    pdf_reader = PyPDF2.PdfReader(uploaded_resume)
    for page in pdf_reader.pages:
        resume_text += page.extract_text()
    st.success("Resume uploaded successfully!")

if uploaded_jd and uploaded_resume:
    st.write("Both files received. Matching logic can run here.")
