from fastapi import FastAPI
from pydantic import BaseModel
from docx import Document
from jinja2 import Template

app = FastAPI(title="Resume Tailor")

class TailorRequest(BaseModel):
    profile: dict
    job: dict

@app.post("/tailor")
async def tailor(req: TailorRequest):
    # Simple template-based tailoring
    doc = Document()
    doc.add_paragraph("Tailored Resume for " + req.job.get('title', ''))
    # TODO: Advanced matching
    return {"status": "success", "message": "Resume tailored. Download link in production."}