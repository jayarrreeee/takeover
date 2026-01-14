def normalize_quote(quote: dict):
q = quote["quoteResponse"]["result"][0]
return {
"price": q.get("regularMarketPrice"),
"market_cap": q.get("marketCap"),
"shares_outstanding": q.get("sharesOutstanding")
}
