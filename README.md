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
1️. Clone the Repository

2️. Create a Virtual Environment

3️. Activate the Virtual Environment

4️. Install Dependencies

5️. Download Spacy NLP Model

# How to Use the Application
1️. Enter the Job Description in the text box.
2️. Upload Resumes (PDF format only).
3️. Click "Rank Resumes" to initiate the screening process.
4️. View the Ranked List of Candidates with similarity scores.

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

1. Resume Text Extraction
Uses PyPDF2 to extract text from uploaded PDF resumes.
Filters out unnecessary formatting and retains only textual content.

2. Text Preprocessing
Tokenization, lowercasing, and stopword removal using Spacy.
Converts resumes and job descriptions into a structured format.

3️. Feature Engineering (TF-IDF)
TF-IDF Vectorization is applied to transform textual data into numerical representations.

This ensures each word’s importance is weighed properly.

4️. Resume Ranking (Cosine Similarity)
Measures the similarity between the job description vector and resume vectors.

Returns a sorted list of resumes, ranked by relevance.

# Results

![image](https://github.com/user-attachments/assets/bf199700-b685-41c9-9aa2-dd24f57b4ecd)
![image](https://github.com/user-attachments/assets/a36e42ab-bf38-4623-8213-3da58a69e455)

# How to Run the code



# Future Improvements

a. Deep Learning Models for Better Matching
Instead of relying only on TF-IDF, future versions will integrate BERT (Bidirectional Encoder Representations from Transformers) and GPT-based models to understand the context more effectively.

b. Multilingual Support
Currently, the system processes only English resumes. Future updates will include multi-language support using mBERT (Multilingual BERT).

c. Enhanced Resume Scoring
Weighting different sections (Experience, Education, Skills) separately.

Using structured data to improve scoring accuracy.

d. Explainable AI (XAI) for Transparency
Integrate SHAP (Shapley Additive Explanations) to provide insights into ranking decisions.

e. Integration with Applicant Tracking Systems (ATS)
This system can be expanded to work directly with ATS platforms for seamless hiring workflows
