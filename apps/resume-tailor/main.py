from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Resume Tailor")

@app.post("/tailor")
async def tailor(profile: dict, job: dict):
    # TODO: Templating logic
    return {"status": "tailored", "resume_url": "generated.docx"}