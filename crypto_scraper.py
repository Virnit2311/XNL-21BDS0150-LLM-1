import requests

class CryptoScraper:
    def fetch_crypto_price(self, symbol):
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}USDT"
        response = requests.get(url)
        return response.json()

scraper = CryptoScraper()
print(scraper.fetch_crypto_price("BTC"))
