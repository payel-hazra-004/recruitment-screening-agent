#!/usr/bin/env python
# coding: utf-8

# In[5]:





# In[6]:


import re
import PyPDF2
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# In[7]:


def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text


# In[8]:


def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text


# In[9]:


SKILLS = [
    "python", "java", "c++", "machine learning",
    "deep learning", "data analysis", "sql",
    "excel", "communication", "tensorflow",
    "pytorch", "nlp", "power bi", "tableau"
]


# In[10]:


def extract_skills(text):
    found_skills = []
    for skill in SKILLS:
        if skill in text:
            found_skills.append(skill)
    return found_skills


# In[11]:


def keyword_match_score(jd_skills, resume_skills):
    matched = set(jd_skills).intersection(set(resume_skills))
    
    if len(jd_skills) == 0:
        return 0, matched
    
    score = len(matched) / len(jd_skills)
    return round(score * 100, 2), matched


# In[12]:


def semantic_match_score(jd_text, resume_text):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([jd_text, resume_text])
    
    similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    return round(similarity * 100, 2)


# In[13]:


jd_text_path =  r"C:\Users\Payel\Desktop\INTEL GEN AI\Recruitment Screening Agent\sample data\JD.txt"
resume_path = r'C:\Users\Payel\Desktop\INTEL GEN AI\Recruitment Screening Agent\sample data\resume.pdf'


# In[14]:


with open(jd_text_path, "r", encoding="utf-8") as file:
    jd_text = file.read()

resume_text = extract_text_from_pdf(resume_path)


# In[15]:


jd_text = clean_text(jd_text)
resume_text = clean_text(resume_text)


# In[16]:


jd_skills = extract_skills(jd_text)
resume_skills = extract_skills(resume_text)


# In[17]:


keyword_score, matched_skills = keyword_match_score(jd_skills, resume_skills)

semantic_score = semantic_match_score(jd_text, resume_text)

final_score = (0.4 * keyword_score) + (0.6 * semantic_score)
final_score = round(final_score, 2)


# In[18]:


if final_score >= 75:
    decision = "Highly Recommended"
elif final_score >= 50:
    decision = "Moderately Suitable"
else:
    decision = "Not Recommended"


# In[19]:


print("\n===== RECRUITMENT SCREENING RESULT =====\n")

print("Job Description Skills:", jd_skills)
print("Resume Skills:", resume_skills)
print("Matched Skills:", matched_skills)

print("\nKeyword Score:", keyword_score, "%")
print("Semantic Score:", semantic_score, "%")
print("Final ATS Score:", final_score, "%")

print("\nFinal Decision:", decision)


# In[ ]:




