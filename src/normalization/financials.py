def extract_financials(filing: dict):
return {
"revenue": filing.get("Revenues"),
"net_income": filing.get("NetIncomeLoss")
}
