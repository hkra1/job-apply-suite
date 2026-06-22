from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Application Automator")

@app.post("/apply")
async def apply(job_link: str):
    # TODO: Playwright automation with warnings
    return {"status": "submitted", "note": "Human review recommended for CAPTCHA"}