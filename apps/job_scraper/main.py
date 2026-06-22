from fastapi import FastAPI
from pydantic import BaseModel
from jobspy import scrape_jobs
import pandas as pd

app = FastAPI(title="Job Scraper")

class ScrapeRequest(BaseModel):
    search_term: str
    results_wanted: int = 10

class Job(BaseModel):
    title: str
    company: str
    location: str
    link: str
    description: str = ""
    requirements: str = ""

@app.post("/scrape")
async def scrape(req: ScrapeRequest):
    jobs = scrape_jobs(search_term=req.search_term, results_wanted=req.results_wanted)
    df = pd.DataFrame(jobs)
    # Clean to table format
    return {"jobs": df.to_dict(orient="records"), "markdown_table": df.to_markdown()}