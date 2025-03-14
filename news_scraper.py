import requests
from bs4 import BeautifulSoup

class NewsScraper:
    def fetch_financial_news(self):
        url = "https://www.bloomberg.com/markets"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")

        headlines = [headline.text for headline in soup.find_all("h3")[:5]]
        return headlines

scraper = NewsScraper()
print(scraper.fetch_financial_news())
