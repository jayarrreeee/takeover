# Market Takeover Data Pipeline


This repository ingests publicly available data on US public companies,
normalizes it into a canonical schema, and stores it for downstream analytics.


## Pipeline Stages
1. Ingest raw data (SEC, Yahoo Finance)
2. Store raw payloads
3. Normalize into canonical tables
4. Prepare for feature engineering


## Run
```bash
python src/orchestration/run_pipeline.py
