### AI-powered-Resume-Screening-and-Ranking-System

# Overview
Recruitment processes often involve screening hundreds of resumes manually, which is both time-consuming and prone to biases. This AI-powered Resume Screening and Ranking System automates resume evaluation using Natural Language Processing (NLP) and Machine Learning (ML) to rank candidates based on their relevance to a given job description.

By leveraging TF-IDF (Term Frequency-Inverse Document Frequency) and cosine similarity, this system provides recruiters with an efficient, unbiased, and data-driven method to shortlist candidates. The project features an interactive Streamlit-based UI, making it easy for HR professionals to upload resumes and obtain ranked results instantly.

# Features
✔ Automated Resume Screening – Eliminates the need for manual shortlisting.
✔ Text Extraction from PDF – Parses and processes resume content efficiently.
✔ TF-IDF Vectorization – Converts resumes and job descriptions into numerical vectors.
✔ Cosine Similarity Matching – Measures how closely a resume matches the job description.
✔ Interactive Web Application – Simple Streamlit UI for easy resume uploads and analysis.
✔ Multi-Resume Support – Upload multiple resumes at once and receive ranked results.
✔ Scalable & Fast – Handles large datasets efficiently with optimized computations.

# Installation & Setup
1️⃣ Clone the Repository

2️⃣ Create a Virtual Environment

3️⃣ Activate the Virtual Environment

4️⃣ Install Dependencies

5️⃣ Download Spacy NLP Model

# How to Use the Application
1️⃣ Enter the Job Description in the text box.
2️⃣ Upload Resumes (PDF format only).
3️⃣ Click "Rank Resumes" to initiate the screening process.
4️⃣ View the Ranked List of Candidates with similarity scores.

The higher the similarity score, the better the resume matches the job description.

Technologies Used

Python 
Streamlit
Pandas 
Scikit-learn
Spacy 
PyPDF2 
TF-IDF 
Cosine Similarity 

# Methodology

1️⃣ Resume Text Extraction
Uses PyPDF2 to extract text from uploaded PDF resumes.

Filters out unnecessary formatting and retains only textual content.

2️⃣ Text Preprocessing
Tokenization, lowercasing, and stopword removal using Spacy.

Converts resumes and job descriptions into a structured format.

3️⃣ Feature Engineering (TF-IDF)
TF-IDF Vectorization is applied to transform textual data into numerical representations.

This ensures each word’s importance is weighed properly.

4️⃣ Resume Ranking (Cosine Similarity)
Measures the similarity between the job description vector and resume vectors.

Returns a sorted list of resumes, ranked by relevance.

🌍 Future Improvements
🔹 Deep Learning Models for Better Matching
Instead of relying only on TF-IDF, future versions will integrate BERT (Bidirectional Encoder Representations from Transformers) and GPT-based models to understand the context more effectively.

🔹 Multilingual Support
Currently, the system processes only English resumes. Future updates will include multi-language support using mBERT (Multilingual BERT).

🔹 Enhanced Resume Scoring
Weighting different sections (Experience, Education, Skills) separately.

Using structured data to improve scoring accuracy.

🔹 Explainable AI (XAI) for Transparency
Integrate SHAP (Shapley Additive Explanations) to provide insights into ranking decisions.

🔹 Integration with Applicant Tracking Systems (ATS)
This system can be expanded to work directly with ATS platforms for seamless hiring workflows
