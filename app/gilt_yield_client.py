# app/gilt_yield_client.py

from fred_client import get_uk_gilt_yields as fred_fetch
from kaggle_client import get_uk_gilt_yields as kaggle_fetch

def get_uk_gilt_yields():
    try:
        return fred_fetch()
    except Exception:
        return kaggle_fetch()
