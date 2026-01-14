from src.ingestion.sec_edgar import fetch_company_filings
from src.ingestion.yahoo_finance import fetch_quote
from src.normalization.companies import normalize_company


CIKS = ["0000320193"] # Apple example


for cik in CIKS:
filings = fetch_company_filings(cik)
company = normalize_company(filings)
print(company)
