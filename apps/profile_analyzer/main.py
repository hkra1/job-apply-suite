from fastapi import FastAPI
app = FastAPI(title='Profile Analyzer')
@app.get('/health')
def health(): return {'status': 'ok'}
# TODO: Implement resume parsing + LinkedIn scrape