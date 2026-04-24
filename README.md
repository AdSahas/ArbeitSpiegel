# 🧠 ArbeitSpiegel — AI Job Application Copilot

ArbeitSpiegel, meaning "Job Mirror" in German, is an AI-powered job application assistant that analyzes CVs against job descriptions, rewrites resumes, generates tailored cover letters, and performs realistic recruiter-style skill gap analysis using LLMs. Designed for the German market, it will help you get closer to your dream role in seconds. 

Built with:
- FastAPI
- Streamlit
- Groq API
- Llama 3.3

---

# 🚀 Features

## 📄 CV Matching & Optimization
- Compares CVs against job descriptions
- Generates recruiter-style compatibility ratings
- Rewrites CVs for stronger alignment
- Improves clarity, structure, and ATS compatibility

## ✉️ Tailored Cover Letter Generation
- Generates role-specific cover letters
- Aligns experience with job requirements
- Maintains realistic and professional tone

## 🔍 Skill Gap Analysis
- Identifies realistic missing qualifications
- Recognizes transferable experience
- Provides actionable improvement suggestions

## 🧠 Semantic Matching

The system uses semantic reasoning instead of simple keyword matching.

Examples:
- “OpenAI API” → practical LLM experience
- “ChromaDB” → vector database exposure
- “semantic retrieval” → RAG/retrieval systems
- Hospitality experience → customer-facing support experience

## ⚡ Fast Inference

Powered by Groq-hosted Llama 3.3 models for low-latency responses.

---

# 💡 Why This Project?

Most applicants spend hours manually rewriting resumes for each job application without understanding:
- why their CV does or does not match a role
- which skills are actually missing
- how recruiters interpret transferable experience

Many existing resume tools rely heavily on keyword matching.

ArbeitSpiegel was built to behave more like a recruiter-style assistant by:
- recognizing semantic equivalents
- identifying transferable experience
- avoiding fabricated achievements
- generating more realistic and believable CV rewrites

The goal is not just ATS optimization — it is producing applications that feel authentic, targeted, and recruiter-friendly.

---

# 🧠 Design Principles

- Semantic matching instead of pure keyword matching
- Evidence-based rewriting
- Recruiter-style evaluation logic
- Recognition of transferable experience
- Human-readable and ATS-friendly formatting
- Realistic, non-exaggerated outputs

---

# ⚙️ Tech Stack

- Python
- FastAPI
- Streamlit
- Groq API
- Llama 3.3
- Pydantic
- Requests

---

# 🏗️ Architecture

```text
User Input (CV + Job Description)
        ↓
Streamlit Frontend
        ↓
FastAPI Backend
        ↓
Prompt Engineering Layer
        ↓
Groq API (Llama 3.3)
        ↓
Structured AI Outputs
```

---

# 📦 Project Structure

```text
ArbeitSpiegel/
│
├── backend/
│   ├── llm.py
│   ├── main.py
│   └── prompts.py
│
└── frontend/
    └── app.py
```

---

# 🧪 Example Outputs

## 📄 CV Improvement

### Original
```text
Built an internal search tool for company documents
```

### Improved
```text
Developed a retrieval-based document assistant using semantic search and document processing workflows
```

---

## ✉️ Cover Letter Example

### Generated Output
```text
My experience building backend systems and customer-facing tools aligns strongly with the responsibilities of this role. I have worked on API integrations, workflow coordination, and customer interaction within fast-paced environments, and I am eager to apply those skills in a customer success setting.
```

---

## 🔍 Skill Gap Analysis Example

### Identified Gaps
- CRM platform experience
- Advanced German proficiency
- Customer success workflow exposure

### Suggested Improvements
- Complete a HubSpot or Salesforce CRM certification
- Improve German proficiency through structured language practice
- Build familiarity with onboarding and customer retention workflows

# ⚙️ How to Run

## 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 2️⃣ Add a Groq API Key

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

---

## 3️⃣ Run the Backend

```bash
uvicorn main:app --reload
```

---

## 4️⃣ Run the Frontend

```bash
streamlit run app.py
```

---

# 📌 Current Capabilities

✅ CV analysis and scoring

✅ Recruiter-style CV rewriting

✅ Cover letter generation

✅ Skill gap analysis

✅ Semantic skill matching

✅ Transferable experience recognition

---

# 🔮 Future Improvements

- PDF/DOCX parsing
- Multi-CV ranking
- Recruiter feedback calibration
- LinkedIn/GitHub integration
- Exportable application packages
- Interview question generation
- Domain-specific optimization

---

# 🤝 Contributions

Contributions, suggestions, and improvements are welcome.

Feel free to fork the repository, open issues, or submit pull requests.

---

# 📜 License

This project is intended for educational, research, and portfolio purposes.
