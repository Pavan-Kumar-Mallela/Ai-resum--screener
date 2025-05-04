import streamlit as st
import fitz  # PyMuPDF
import os
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="AI Resume Screener", layout="wide")
st.title("📄 AI Resume Screener")

# --- Helper functions ---
def extract_text_from_pdf(uploaded_file):
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text.lower()

def preprocess_text(text):
    text = re.sub(r'\W+', ' ', text)  # remove special characters
    return text.lower()

def match_score(resume_text, jd_text):
    vectorizer = CountVectorizer().fit_transform([resume_text, jd_text])
    vectors = vectorizer.toarray()
    return cosine_similarity([vectors[0]], [vectors[1]])[0][0] * 100  # percentage

# --- Job Description Input ---
with st.sidebar:
    st.header("🧾 Job Description")
    jd_input = st.text_area("Paste the job description here...", height=250)

# --- File Upload ---
uploaded_files = st.file_uploader("Upload Resume PDFs", type=["pdf"], accept_multiple_files=True)

if st.button("Evaluate"):
    if not jd_input.strip():
        st.warning("Please paste a job description to evaluate resumes.")
    elif not uploaded_files:
        st.warning("Please upload at least one resume file.")
    else:
        results = []
        jd_clean = preprocess_text(jd_input)

        for file in uploaded_files:
            resume_text = extract_text_from_pdf(file)
            resume_clean = preprocess_text(resume_text)
            score = match_score(resume_clean, jd_clean)
            results.append((file.name, round(score, 2)))

        results.sort(key=lambda x: x[1], reverse=True)

        st.success("✅ Evaluation complete. Ranked resumes below:")
        for name, score in results:
            st.write(f"**{name}** — Match Score: 🔍 **{score:.2f}%**")
