# Recruitment Screening Agent

## 📌 Overview
Recruitment teams often spend a significant amount of time manually screening resumes, which can be slow, inconsistent, and biased.  
This project presents an **AI-powered Recruitment Screening Agent** that automates the initial resume screening process by matching candidate profiles with job descriptions and ranking candidates based on relevance.

---

## 🎯 Problem Statement
Manual resume screening:
- Is time-consuming for HR teams  
- Can introduce unconscious bias  
- Makes it difficult to fairly compare large numbers of candidates  

There is a need for an automated, transparent, and efficient screening system.

---

## 💡 Solution
The Recruitment Screening Agent analyzes resumes and job descriptions using NLP and basic ML techniques to:
- Extract relevant skills
- Match candidate skills with job requirements
- Generate a matching score
- Rank candidates for shortlisting

This helps recruiters make **faster and more data-driven decisions**.

---

## 🚀 Features
- Resume text parsing (PDF/DOCX/Text)
- Job Description (JD) analysis
- Skill extraction using NLP
- Resume–JD matching score
- Candidate ranking
- Explainable results (why a candidate was shortlisted or rejected)

---

## 🧠 Tech Stack
- Python  
- Natural Language Processing (NLP)  
- scikit-learn  
- pandas, numpy  
- spaCy / NLTK  
- Streamlit / Flask (optional for UI)

---

## 🛠️ How It Works
1. Resume and job description are provided as input  
2. Text is cleaned and processed using NLP  
3. Skills are extracted from both resume and JD  
4. A matching score is calculated based on skill overlap  
5. Candidates are ranked based on relevance  

---

## ▶️ How to Run
```bash
pip install -r requirements.txt
python app.py
