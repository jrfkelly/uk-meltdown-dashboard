# app/collect_gilts.py

from gilt_yield_client import get_uk_gilt_yields
from db_connection import get_engine

def ingest_gilt_data():
    df = get_uk_gilt_yields()
    df.to_sql("uk_gilt_yields", get_engine(), if_exists="replace", index=False)

if __name__ == "__main__":
    ingest_gilt_data()
