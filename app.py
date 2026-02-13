import streamlit as st
import re
import PyPDF2
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="Recruitment Screening Agent")
st.title("📄 Recruitment Screening Agent")
st.write("Upload Job Description (TXT) and Resume (PDF) to evaluate candidate.")


# -------------------------------
# FUNCTIONS
# -------------------------------

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text


SKILLS = [
    "python", "java", "c++", "machine learning",
    "deep learning", "data analysis", "sql",
    "excel", "communication", "tensorflow",
    "pytorch", "nlp", "power bi", "tableau"
]


def extract_skills(text):
    found_skills = []
    for skill in SKILLS:
        if skill in text:
            found_skills.append(skill)
    return found_skills


def keyword_match_score(jd_skills, resume_skills):
    matched = set(jd_skills).intersection(set(resume_skills))

    if len(jd_skills) == 0:
        return 0, matched

    score = len(matched) / len(jd_skills)
    return round(score * 100, 2), matched


def semantic_match_score(jd_text, resume_text):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([jd_text, resume_text])

    similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    return round(similarity * 100, 2)


# -------------------------------
# FILE UPLOAD SECTION
# -------------------------------

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


# -------------------------------
# PROCESSING SECTION
# -------------------------------

if uploaded_jd and uploaded_resume:

    jd_text = clean_text(jd_text)
    resume_text = clean_text(resume_text)

    jd_skills = extract_skills(jd_text)
    resume_skills = extract_skills(resume_text)

    keyword_score, matched_skills = keyword_match_score(jd_skills, resume_skills)
    semantic_score = semantic_match_score(jd_text, resume_text)

    final_score = (0.4 * keyword_score) + (0.6 * semantic_score)
    final_score = round(final_score, 2)

    if final_score >= 75:
        decision = "✅ Highly Recommended"
    elif final_score >= 50:
        decision = "⚖️ Moderately Suitable"
    else:
        decision = "❌ Not Recommended"

    # -------------------------------
    # DISPLAY RESULTS
    # -------------------------------

    st.subheader("📊 Recruitment Screening Result")

    st.write("**Job Description Skills:**", jd_skills)
    st.write("**Resume Skills:**", resume_skills)
    st.write("**Matched Skills:**", list(matched_skills))

    st.write("### Scores")
    st.write("Keyword Score:", keyword_score, "%")
    st.write("Semantic Score:", semantic_score, "%")
    st.write("Final ATS Score:", final_score, "%")

    st.success(f"Final Decision: {decision}")
