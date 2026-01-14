def normalize_company(sec_payload: dict):
return {
"cik": sec_payload.get("cik"),
"name": sec_payload.get("name"),
"ticker": sec_payload.get("tickers", [None])[0],
"industry": sec_payload.get("sicDescription")
}
