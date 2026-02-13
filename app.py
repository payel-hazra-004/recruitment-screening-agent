# app.py
import re
import streamlit as st
import PyPDF2
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -------------------------------
# Helper Functions
# -------------------------------

def extract_text_from_pdf(file):
    """Extract text from uploaded PDF"""
    text = ""
    pdf_reader = PyPDF2.PdfReader(file)
    for page in pdf_reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text
    return text

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
# Streamlit UI
# -------------------------------
st.set_page_config(page_title="AI Recruitment Screening Agent", layout="wide")
st.title("🚀 AI-Powered Resume Screening Agent")
st.subheader("Upload Job Description and Resume to see ATS-style scoring ✨")
st.markdown("---")

# File upload
jd_file = st.file_uploader("Upload Job Description (.txt)", type=["txt"])
resume_file = st.file_uploader("Upload Resume (.pdf)", type=["pdf"])

if jd_file and resume_file:
    # Read JD text
    jd_text = jd_file.read().decode("utf-8")
    jd_text = clean_text(jd_text)
    
    # Read resume text
    resume_text = extract_text_from_pdf(resume_file)
    resume_text = clean_text(resume_text)
    
    # Extract skills
    jd_skills = extract_skills(jd_text)
    resume_skills = extract_skills(resume_text)
    
    # Keyword & Semantic scoring
    keyword_score, matched_skills = keyword_match_score(jd_skills, resume_skills)
    semantic_score = semantic_match_score(jd_text, resume_text)
    
    # Final ATS score (weighted)
    final_score = round((0.4 * keyword_score) + (0.6 * semantic_score), 2)
    
    # Decision
    if final_score >= 75:
        decision = "Highly Recommended ✅"
    elif final_score >= 50:
        decision = "Moderately Suitable ⚡"
    else:
        decision = "Not Recommended ❌"
    
    # -------------------------------
    # Display Results in Streamlit
    # -------------------------------
    st.header("📊 Recruitment Screening Result")
    
    col1, col2 = st.columns(2)
    col1.metric("Keyword Score", f"{keyword_score}%")
    col2.metric("Semantic Score", f"{semantic_score}%")
    
    st.subheader("Matched Skills")
    if matched_skills:
        st.write(", ".join(matched_skills))
    else:
        st.write("No matched skills found.")
    
    st.subheader("Final ATS Score")
    st.progress(final_score / 100)
    st.markdown(f"**Decision:** {decision}")
    
    # Optional: show all skills detected
    with st.expander("View all detected skills"):
        st.write("JD Skills:", jd_skills)
        st.write("Resume Skills:", resume_skills)

else:
    st.info("Upload both a Job Description (.txt) and Resume (.pdf) to get results.")
