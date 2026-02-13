# 🤖 Recruitment Screening Agent

## 📌 Overview
Recruitment teams often spend a significant amount of time manually screening resumes, which can be slow, inconsistent, and subjective.  

This project presents an **AI-powered Recruitment Screening Agent (ATS Scoring System)** that automates the initial resume evaluation process by comparing a candidate’s resume with a given Job Description (JD) and generating a relevance score.

The system uses **Natural Language Processing (NLP)** techniques to measure both skill overlap and contextual similarity between the resume and the job description.

---

## 🎯 Problem Statement

Manual resume screening:

- Is time-consuming for HR teams  
- May introduce unconscious bias  
- Makes it difficult to consistently evaluate candidates  
- Lacks standardized scoring  

There is a need for an automated, transparent, and efficient resume evaluation system.

---

## 💡 Solution

The Recruitment Screening Agent analyzes resumes and job descriptions using NLP techniques to:

- Extract resume text from PDF files  
- Clean and preprocess textual data  
- Extract relevant technical skills  
- Calculate a keyword matching score  
- Compute semantic similarity using TF-IDF and Cosine Similarity  
- Generate a final ATS score  
- Provide a hiring recommendation  

This enables **objective and data-driven candidate screening**.

---

## 🚀 Features

- Resume text extraction from PDF  
- Job Description (JD) text analysis  
- Skill extraction using predefined skill list  
- Keyword-based matching score  
- Semantic similarity scoring (TF-IDF + Cosine Similarity)  
- Weighted final ATS score  
- Automated recommendation:
  - Highly Recommended  
  - Moderately Suitable  
  - Not Recommended  

---

## 🧠 Tech Stack

- Python  
- Natural Language Processing (NLP)  
- scikit-learn  
- PyPDF2  
- numpy  
- Regular Expressions (re)  

---

## 🛠️ How It Works

1. Job Description (JD.txt) is provided as input  
2. Resume (PDF) is uploaded  
3. Text is extracted and cleaned  
4. Skills are extracted from both JD and resume  
5. Keyword matching score is calculated  
6. Semantic similarity score is computed using TF-IDF + Cosine Similarity  
7. Final ATS score is calculated using weighted formula  
8. Hiring recommendation is displayed  

---

## 🧮 Scoring Formula

**Keyword Score:**
Keyword Score = (Matched Skills / Total JD Skills) × 100

**Semantic Similarity Score:**
- Calculated using TF-IDF vectorization
- Cosine similarity between resume and JD vectors

**Final ATS Score:**
Final ATS Score = (0.4 × Keyword Score) + (0.6 × Semantic Score)



---

## ▶️ How to Run

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

2️⃣ Run the Notebook or Script

If using Jupyter Notebook:
```bash
jupyter notebook screening_agent.ipynb
```
📌 Sample Output
```bash
===== RECRUITMENT SCREENING RESULT =====

JD Skills: ['python', 'machine learning', 'sql']
Resume Skills: ['python', 'sql', 'excel']

Matched Skills: ['python', 'sql']

Keyword Score: 66.67%
Semantic Score: 78.45%
Final ATS Score: 73.94%

Decision: Moderately Suitable
```
🔮 Future Improvements

- Replace TF-IDF with BERT or Sentence Transformers

- Add dynamic skill extraction (NER-based)

- Enable multi-resume ranking

- Build web interface using Streamlit

- Add database integration for storing candidates

👩‍💻 Author

Payel Hazra
Aspiring Data Scientist | Machine Learning Enthusiast
