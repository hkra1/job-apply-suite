from fastapi import FastAPI, UploadFile, Form
from pydantic import BaseModel
import pdfplumber
from docx import Document

app = FastAPI(title="Profile Analyzer")

class AnalysisResponse(BaseModel):
    skills: list[str]
    experience: list[dict]
    education: list[str]

@app.post("/analyze")
async def analyze(resume: UploadFile, linkedin_url: str = Form(None)):
    # Minimal resume parsing
    text = ""
    if resume.filename.endswith('.pdf'):
        with pdfplumber.open(resume.file) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
    # TODO: Add LinkedIn scraping with Playwright
    return AnalysisResponse(skills=["Python", "FastAPI"], experience=[{"role": "Dev"}], education=["BS"])