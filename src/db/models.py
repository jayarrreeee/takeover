from sqlalchemy import (
Table, Column, Integer, String, Date, Float, MetaData, JSON
)


metadata = MetaData()


companies = Table(
"companies",
metadata,
Column("company_id", Integer, primary_key=True),
Column("cik", String, unique=True),
Column("ticker", String),
Column("name", String),
Column("industry", String)
)


raw_filings = Table(
"raw_filings",
metadata,
Column("id", Integer, primary_key=True),
Column("cik", String),
Column("form_type", String),
Column("period_end", Date),
Column("raw_payload", JSON)
)
