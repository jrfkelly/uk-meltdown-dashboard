# app/fred_client.py

import os
import requests
import pandas as pd

FRED_API_URL = "https://api.stlouisfed.org/fred/series/observations"

def get_uk_gilt_yields():
    api_key = os.getenv("FRED_API_KEY")
    series_id = "IRLTLT01GBM156N"  # UK 10y yield, monthly, not seasonally adjusted

    params = {
        "series_id": series_id,
        "api_key": api_key,
        "file_type": "json",
    }

    resp = requests.get(FRED_API_URL, params=params)
    resp.raise_for_status()

    data = resp.json().get("observations", [])

    df = pd.DataFrame(data)[["date", "value"]]
    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    df.dropna(inplace=True)

    return df
