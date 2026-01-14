import requests


def fetch_quote(ticker: str):
url = f"https://query1.finance.yahoo.com/v7/finance/quote?symbols={ticker}"
r = requests.get(url)
r.raise_for_status()
return r.json()
