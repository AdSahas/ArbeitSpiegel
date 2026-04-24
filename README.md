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

# Demo Output:

## Sample CV:
CURRICULUM VITAE
Jordan Mills
jordan.mills@email.com | LinkedIn: linkedin.com/in/jordanmills | New York, NY
Summary
Data analyst with 5 years of experience turning large, complex datasets into clear business insights. Proven track record in financial services, with deep expertise in SQL, Python, and BI tools. Comfortable presenting to both technical and non-technical audiences.
Experience
Data Analyst → Senior Data Analyst — Meridian Financial, New York, NY (2020–Present)

Built and maintained 15+ Tableau dashboards used daily by C-suite stakeholders
Wrote optimized SQL queries against multi-billion row datasets, reducing report runtime by 40%
Led a 6-month A/B testing program on customer onboarding flows, improving conversion by 18%
Mentored 2 junior analysts and established a team SQL style guide
Collaborated with data engineering to redesign 3 ETL pipelines in dbt

Data Analyst — BrightMetrics, Jersey City, NJ (2019–2020)

Supported marketing and product teams with ad hoc analysis using Python (pandas, numpy)
Created automated weekly reports, saving ~6 hours of manual work per week

Skills
SQL (PostgreSQL, BigQuery), Python (pandas, numpy, matplotlib), Tableau, Power BI, dbt, Git, Excel, A/B Testing, Stakeholder Communication
Education
B.S. Statistics — Rutgers University, 2019
Certifications

Tableau Desktop Specialist (2022)
Google Data Analytics Certificate (2021)

---
## Sample Job Description:
JOB DESCRIPTION
Position: Senior Data Analyst
Company: FinEdge Analytics
Location: New York, NY (Hybrid)
FinEdge Analytics is looking for a Senior Data Analyst to join our growing data team. You will work closely with business stakeholders to translate complex data into actionable insights.
Responsibilities:

Design and maintain dashboards and reports using Tableau and Power BI
Write complex SQL queries to extract and transform large datasets
Collaborate with data engineers on pipeline improvements
Lead A/B testing initiatives and present findings to leadership
Mentor junior analysts on best practices

Requirements:

4+ years of experience in data analysis
Proficiency in SQL, Python (pandas, numpy)
Experience with Tableau or Power BI
Strong communication and stakeholder management skills
Experience in fintech or financial services is a plus
Bachelor's degree in a quantitative field
---

## CV Analysis and Rewritten CV

Rating: 9/10

Explanation: The CV strongly matches the job description, with relevant experience in data analysis, proficiency in required skills such as SQL, Python, and Tableau, and a strong track record of presenting insights to stakeholders. The candidate's experience in financial services and fintech is also a plus. The only minor gap is that the CV could be more explicit about the candidate's experience with Power BI, although it is mentioned as a skill.

Improved CV: CURRICULUM VITAE Jordan Mills jordan.mills@email.com | LinkedIn: linkedin.com/in/jordanmills | New York, NY

Summary Data analyst with 5 years of experience turning large, complex datasets into clear business insights. Proven track record in financial services, with deep expertise in SQL, Python, and BI tools. Comfortable presenting to both technical and non-technical audiences.

Experience Data Analyst → Senior Data Analyst — Meridian Financial, New York, NY (2020–Present)

    Built and maintained 15+ Tableau dashboards used daily by C-suite stakeholders
    Wrote optimized SQL queries against multi-billion row datasets, reducing report runtime by 40%
    Led a 6-month A/B testing program on customer onboarding flows, improving conversion by 18%
    Mentored 2 junior analysts and established a team SQL style guide
    Collaborated with data engineering to redesign 3 ETL pipelines in dbt

Data Analyst — BrightMetrics, Jersey City, NJ (2019–2020)

    Supported marketing and product teams with ad hoc analysis using Python (pandas, numpy)
    Created automated weekly reports, saving ~6 hours of manual work per week
    Utilized Power BI to create interactive dashboards for business stakeholders

Skills SQL (PostgreSQL, BigQuery), Python (pandas, numpy, matplotlib), Tableau, Power BI, dbt, Git, Excel, A/B Testing, Stakeholder Communication

Education B.S. Statistics — Rutgers University, 2019

Certifications Tableau Desktop Specialist (2022) Google Data Analytics Certificate (2021)

---
## Cover Letter

Dear Hiring Manager,

As a seasoned data analyst with a strong background in financial services, I am excited to apply for the Senior Data Analyst position at FinEdge Analytics. With 5 years of experience in turning complex datasets into clear business insights, I am confident in my ability to drive actionable recommendations for business stakeholders. My expertise in SQL, Python, and BI tools such as Tableau and Power BI aligns well with the job requirements. I have a proven track record of designing and maintaining dashboards, writing optimized SQL queries, and collaborating with data engineers to improve pipeline efficiency.

I am particularly drawn to this role because of the opportunity to work closely with business stakeholders and lead A/B testing initiatives, presenting findings to leadership. My experience in mentoring junior analysts and establishing best practices will also enable me to make a positive impact on the team. I am excited about the prospect of joining FinEdge Analytics and contributing my skills and experience to drive business growth. I look forward to discussing my application and how I can contribute to the company's success.

Sincerely, Jordan Mills
Skill Gap Analysis

---
## Identified Skill Gaps:

    No direct experience with cloud-based data platforms or big data technologies beyond SQL and dbt is mentioned, which might be expected in a senior data analyst role, especially in a fintech company.
    No explicit experience with data storytelling or presenting complex data insights to non-technical stakeholders is highlighted, although there is mention of presenting to both technical and non-technical audiences.
    The CV does not explicitly mention experience with machine learning, statistical modeling, or advanced analytics techniques that are often expected in senior data analyst roles.
    No experience with Agile methodologies or version control systems beyond Git is mentioned, which could be beneficial in a collaborative data team environment.

Actionable Advice:

    Consider taking courses or gaining experience with cloud-based data platforms such as AWS, GCP, or Azure to enhance your skill set and stay competitive in the market.
    Develop a portfolio of examples that demonstrate your ability to present complex data insights to non-technical stakeholders, such as writing blog posts or creating visual presentations.
    Pursue additional training or certifications in machine learning, statistical modeling, or advanced analytics techniques to enhance your analytical skills and stay up-to-date with industry trends.
    Highlight any experience with Agile methodologies or version control systems beyond Git, and consider gaining experience with tools like Jira, Asana, or GitHub to improve collaboration and project management skills.
