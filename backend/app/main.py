from fastapi import FastAPI
from pydantic import BaseModel
from newspaper import Article

app = FastAPI()

class ScrapeRequest(BaseModel):
    url: str

@app.get("/")
def home():
    return {"message": "AI News Aggregator Backend is Running!"}

@app.post("/scrape")
def scrape_article(request: ScrapeRequest):
    try:
        article = Article(request.url)
        article.download()
        article.parse()
        return {
            "title": article.title,
            "publish_date": article.publish_date,
            "summary": article.text[:300] + "..." # First 300 chars
        }
    
    except Exception as e:
        return {"error": str(e)}