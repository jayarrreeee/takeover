CREATE TABLE companies (
company_id SERIAL PRIMARY KEY,
cik TEXT UNIQUE,
ticker TEXT,
name TEXT,
industry TEXT
);
