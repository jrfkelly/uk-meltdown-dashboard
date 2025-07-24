# dashboard.py

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
from db_connection import get_engine

app = dash.Dash(__name__)

def fetch_data():
    try:
        query = "SELECT date, value FROM uk_gilt_yields ORDER BY date"
        return pd.read_sql(query, get_engine())
    except Exception:
        return pd.DataFrame(columns=["date", "value"])

app.layout = html.Div([
    html.H1("UK 10-Year Gilt Yields"),
    html.Button("Refresh", id="refresh-btn", n_clicks=0),
    dcc.Graph(id="yield-graph")
])

@app.callback(
    Output("yield-graph", "figure"),
    Input("refresh-btn", "n_clicks")
)
def update_graph(_):
    df = fetch_data()
    return {
        "data": [{
            "x": df["date"],
            "y": df["value"],
            "type": "line",
            "name": "10Y Yield"
        }],
        "layout": {
            "title": "UK 10Y Gilt Yield Over Time"
        }
    }

if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8050, debug=True)
