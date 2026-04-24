# AI Job Application Copilot (LLM-powered)

An AI-powered web application that helps users optimize job applications using LLMs.  
It generates improved CV bullet points, tailored cover letters, and skill gap analysis based on a given job description.

Built with **FastAPI + Streamlit + Llama 3.3-70b-versatile (via Groq API)**.

---

## 🚀 Features

- 📄 CV optimization tailored to job descriptions  
- ✉️ Automated cover letter generation  
- 🔍 Skill gap analysis (missing skills + improvement suggestions)  
- ⚡ Fast LLM inference using Llama 3.1 via Groq API  
- 🖥️ Simple Streamlit UI for interactive use  
- 🔗 REST API backend using FastAPI  

---

## 🧠 Tech Stack

- Python  
- FastAPI (backend API layer)  
- Streamlit (frontend UI)  
- Groq API (LLM inference)  
- Llama 3.1 (language model)  
- Pydantic (input validation)  
- Requests (API communication)  

---

## 🏗️ Architecture

User Input (CV + Job Description)  
→ FastAPI Backend  
→ Prompt Engineering Layer  
→ Llama 3.1 via Groq API  
→ Structured AI Outputs  
→ Streamlit UI Display  

---

## 📦 Project Structure
ArbeitSpiegel:
    - Backend
        - llm.py
        - main.py
        - prompts.py
    - frontend
     - app.py

# How to use:

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Add a GROQ API key
Create a .env file with the line:
GROQ_API_KEY={add your API key here_}

### 3. Run the backend
```bash
uvicorn main:app --reload
```

### 4. Run the frontend
```bash
streamlit run app.py
```

# 💡 Why This Project?

Applying for jobs today is often frustrating and repetitive. Many applicants struggle with:

* Tailoring resumes for every application
* Understanding why their CV does not match a role
* Identifying missing technical skills
* Writing personalized cover letters repeatedly
* Getting past ATS (Applicant Tracking Systems)

