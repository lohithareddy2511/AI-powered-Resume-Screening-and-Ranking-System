import streamlit as st
from PyPDF2 import PdfReader
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Function to extract text from PDF
def extract_text_from_pdf(file):
    pdf = PdfReader(file)
    text = ""
    for page in pdf.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + " "
    return text.strip()

# Function to rank resumes based on job description
def rank_resumes(job_description, resumes):
    documents = [job_description] + resumes  # Combine JD with resumes
    vectorizer = TfidfVectorizer().fit_transform(documents)
    vectors = vectorizer.toarray()

    # Calculate cosine similarity
    job_description_vector = vectors[0]
    resume_vectors = vectors[1:]  # Skip JD vector
    cosine_similarities = cosine_similarity([job_description_vector], resume_vectors).flatten()
    
    return cosine_similarities

# Streamlit UI
st.title("📄 AI Resume Screening & Candidate Ranking System")

# Job description input
st.header("📌 Job Description")
job_description = st.text_area("Enter the job description:")

# File uploader
st.header("📤 Upload Resumes")
uploaded_files = st.file_uploader("Upload PDF resumes", type=["pdf"], accept_multiple_files=True)

if uploaded_files and job_description:
    st.header("📊 Ranking Resumes")
    
    resumes = []
    file_names = []
    
    for file in uploaded_files:
        text = extract_text_from_pdf(file)
        if text:
            resumes.append(text)
            file_names.append(file.name)
        else:
            st.warning(f"⚠️ Could not extract text from: {file.name}")

    if resumes:
        # Rank resumes
        scores = rank_resumes(job_description, resumes)

        # Display scores in DataFrame
        results = pd.DataFrame({"Resume": file_names, "Score": scores})
        results = results.sort_values(by="Score", ascending=False)

        st.write(results)
    else:
        st.error("❌ No valid text found in uploaded resumes.")

# type: ignore # Run using:
# streamlit run app.py
