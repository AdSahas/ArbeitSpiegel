🧠 ArbeitSpiegel — AI Job Application Copilot

An AI-powered job application assistant that analyzes CVs against job descriptions, rewrites resumes, generates tailored cover letters, and performs realistic recruiter-style skill gap analysis using LLMs.

Built with:

* FastAPI
* Streamlit
* Groq API
* Llama 3.3

⸻

🚀 Features

📄 CV Matching & Optimization

* Compares CVs against job descriptions
* Generates recruiter-style compatibility ratings
* Rewrites CVs for stronger alignment
* Improves clarity, structure, and ATS compatibility

✉️ Tailored Cover Letter Generation

* Generates role-specific cover letters
* Aligns experience with job requirements
* Maintains realistic and professional tone

🔍 Skill Gap Analysis

* Identifies realistic missing qualifications
* Recognizes transferable experience
* Provides actionable improvement suggestions

🧠 Semantic Matching

The system uses semantic reasoning instead of simple keyword matching.

Examples:

* “OpenAI API” → practical LLM experience
* “ChromaDB” → vector database exposure
* “semantic retrieval” → RAG/retrieval systems
* Hospitality experience → customer-facing support experience

⚡ Fast Inference

Powered by Groq-hosted Llama 3.3 models for low-latency responses.

⸻

💡 Why This Project?

Most applicants spend hours manually rewriting resumes for each job application without understanding:

* why their CV does or does not match a role
* which skills are actually missing
* how recruiters interpret transferable experience

Many existing resume tools rely heavily on keyword matching.

ArbeitSpiegel was built to behave more like a recruiter-style assistant by:

* recognizing semantic equivalents
* identifying transferable experience
* avoiding fabricated achievements
* generating more realistic and believable CV rewrites

The goal is not just ATS optimization — it is producing applications that feel authentic, targeted, and recruiter-friendly.

⸻

🧠 Design Principles

* Semantic matching instead of pure keyword matching
* Evidence-based rewriting
* Recruiter-style evaluation logic
* Recognition of transferable experience
* Human-readable and ATS-friendly formatting
* Realistic, non-exaggerated outputs

⸻

⚙️ Tech Stack

* Python
* FastAPI
* Streamlit
* Groq API
* Llama 3.3
* Pydantic
* Requests

⸻

🏗️ Architecture

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

⸻

📦 Project Structure

ArbeitSpiegel/
│
├── Backend/
│   ├── llm.py
│   ├── main.py
│   └── prompts.py
│
└── frontend/
    └── app.py

⸻

🧪 Example CV Improvement

Original Bullet

Answered customer inquiries and redirected calls

Improved Bullet

Provided front-line customer support and coordinated guest inquiries in a fast-paced hospitality environment

⸻

⚙️ How to Run

1️⃣ Install Dependencies

pip install -r requirements.txt

⸻

2️⃣ Add a Groq API Key

Create a .env file:

GROQ_API_KEY=your_api_key_here

⸻

3️⃣ Run the Backend

uvicorn main:app --reload

⸻

4️⃣ Run the Frontend

streamlit run app.py

⸻

📌 Current Capabilities

✅ CV analysis and scoring

✅ Recruiter-style CV rewriting

✅ Cover letter generation

✅ Skill gap analysis

✅ Semantic skill matching

✅ Transferable experience recognition

⸻

🔮 Future Improvements

* PDF/DOCX parsing
* Multi-CV ranking
* Recruiter feedback calibration
* LinkedIn/GitHub integration
* Exportable application packages
* Interview question generation
* Domain-specific optimization

⸻

🤝 Contributions

Contributions, suggestions, and improvements are welcome.

Feel free to fork the repository, open issues, or submit pull requests.

⸻

📜 License

This project is intended for educational, research, and portfolio purposes.
