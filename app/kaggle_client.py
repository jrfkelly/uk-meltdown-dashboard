# app/kaggle_client.py

import pandas as pd

def get_uk_gilt_yields():
    path = "data/uk_10y_gilt_yields.csv"
    df = pd.read_csv(path, usecols=["date", "value"])
    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    df.dropna(inplace=True)
    return df
