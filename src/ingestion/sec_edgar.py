import requests
from src.config.settings import SEC_USER_AGENT


BASE_URL = "https://data.sec.gov/submissions"


def fetch_company_filings(cik: str):
headers = {"User-Agent": SEC_USER_AGENT}
url = f"{BASE_URL}/CIK{cik.zfill(10)}.json"
response = requests.get(url, headers=headers)
response.raise_for_status()
return response.json()
