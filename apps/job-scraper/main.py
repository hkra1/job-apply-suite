from fastapi import FastAPI
from pydantic import BaseModel
from jobspy import scrape_jobs
import pandas as pd

app = FastAPI(title="Job Scraper")

class JobScrapeRequest(BaseModel):
    search_term: str
    location: str = "Remote"

@app.post("/scrape")
async def scrape(req: JobScrapeRequest):
    jobs = scrape_jobs(search_term=req.search_term, location=req.location, results_wanted=10)
    df = pd.DataFrame(jobs)
    return df.to_dict(orient='records')