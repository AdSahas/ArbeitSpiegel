from fastapi import FastAPI
from pydantic import BaseModel

from backend.llm import call_llm
from backend.prompts import cv_prompt, coverLetter_prompt, skillGap_analysis

app = FastAPI()

class Input(BaseModel):
    cv: str
    job: str

@app.post("/analyse")

def analyse(data: Input):
    cv = data.cv
    job = data.job

    cv_result = call_llm(cv_prompt(cv, job))
    cover_letter_result = call_llm(coverLetter_prompt(cv, job))
    skill_gap_result = call_llm(skillGap_analysis(cv, job))

    return {
        "cv_analysis": cv_result,
        "cover_letter": cover_letter_result,
        "skill_gap_analysis": skill_gap_result
    }
