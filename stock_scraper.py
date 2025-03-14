import yfinance as yf

class StockScraper:
    def fetch_stock_price(self, ticker):
        stock = yf.Ticker(ticker)
        data = stock.history(period="1d")
        return data[['Open', 'High', 'Low', 'Close', 'Volume']]

scraper = StockScraper()
print(scraper.fetch_stock_price("AAPL"))
