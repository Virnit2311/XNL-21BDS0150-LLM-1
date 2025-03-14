from fastapi import FastAPI
from llm_agents.llm_router import LLMRouter
from data_ingestion.stock_scraper import StockScraper
from data_ingestion.crypto_scraper import CryptoScraper
from data_ingestion.news_scraper import NewsScraper

app = FastAPI()
llm_router = LLMRouter()
stock_scraper = StockScraper()
crypto_scraper = CryptoScraper()
news_scraper = NewsScraper()

@app.get("/")
def home():
    return {"message": "FinTech LLM API is running!"}

@app.get("/stock/{ticker}")
def get_stock_price(ticker: str):
    return stock_scraper.fetch_stock_price(ticker)

@app.get("/crypto/{symbol}")
def get_crypto_price(symbol: str):
    return crypto_scraper.fetch_crypto_price(symbol)

@app.get("/news")
def get_financial_news():
    return news_scraper.fetch_financial_news()

@app.get("/query_llm/")
def query_llm(model: str, prompt: str):
    return {"response": llm_router.query_llm(model, prompt)}

# Run Server: uvicorn main:app --reload
