# app.py
import streamlit as st
import pandas as pd
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import time

st.set_page_config(
    page_title="AI Recruitment Screening Agent",
    layout="wide",
    page_icon="🤖"
)

# -------------------------------
# Header
# -------------------------------
st.title("🚀 AI-Powered Resume Screening Agent")
st.subheader("Matching resumes with job descriptions… smarter & faster! ✨")
st.markdown("---")

# -------------------------------
# Sidebar Uploads
# -------------------------------
st.sidebar.header("Upload Files")
resume_file = st.sidebar.file_uploader("Upload Resume (.pdf/.docx)", type=["pdf", "docx"])
jd_file = st.sidebar.file_uploader("Upload Job Description (.txt/.pdf)", type=["txt", "pdf"])

st.sidebar.header("Options")
show_wordcloud = st.sidebar.checkbox("Show Word Cloud of Resume")
st.sidebar.header("Credits")
st.sidebar.info("Built by Payel Hazra | Intel GenAI4GenZ")

# -------------------------------
# Processing Section
# -------------------------------
if resume_file and jd_file:
    with st.spinner("Analyzing resume… ✨"):
        time.sleep(2)  # Simulate processing time; replace with your NLP model

    st.success("Analysis Complete ✅")
    
    # -------------------------------
    # Sample Scores (replace with your model)
    # -------------------------------
    keyword_score = np.random.randint(60, 95)  # replace with actual keyword match
    semantic_score = np.random.randint(65, 98)  # replace with actual semantic similarity
    overall_score = int((keyword_score + semantic_score) / 2)

    # -------------------------------
    # Display Scores
    # -------------------------------
    st.subheader("Candidate Match Score")
    st.progress(overall_score / 100)

    col1, col2 = st.columns(2)
    col1.metric("Keyword Match", f"{keyword_score}%")
    col2.metric("Semantic Similarity", f"{semantic_score}%")

    if overall_score > 90:
        st.balloons()  # Fun confetti animation for high score

    # -------------------------------
    # Sample Keyword Highlighting
    # -------------------------------
    resume_text = "Python, Machine Learning, NLP, SQL, Data Analysis, Communication"
    jd_keywords = ["Python", "NLP", "SQL"]

    highlighted = resume_text
    for word in jd_keywords:
        highlighted = highlighted.replace(word, f"**{word}**")

    st.markdown("### Matched Keywords in Resume")
    st.markdown(highlighted)

    # -------------------------------
    # Word Cloud Visualization
    # -------------------------------
    if show_wordcloud:
        st.subheader("Skills Word Cloud")
        wordcloud = WordCloud(width=400, height=200, background_color='white').generate(resume_text)
        fig, ax = plt.subplots()
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis('off')
        st.pyplot(fig)

    # -------------------------------
    # Candidate Ranking Table (for multiple candidates)
    # -------------------------------
    st.subheader("Candidate Ranking")
    data = {
        "Candidate": ["Alice", "Bob", "Charlie"],
        "Keyword Match": [78, 65, 90],
        "Semantic Similarity": [85, 70, 95],
        "Overall Score": [81, 67, 92],
        "Badge": ["🏆 Top Fit", "💡 Potential", "⚡ Strong Candidate"]
    }
    df = pd.DataFrame(data)
    st.dataframe(df.style.highlight_max(axis=0, color='lightgreen'))

else:
    st.info("Upload both a resume and a job description to get started.")
