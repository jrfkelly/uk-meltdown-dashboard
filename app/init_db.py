# app/init_db.py

from sqlalchemy import text
from db_connection import get_engine

DDL = """
CREATE TABLE IF NOT EXISTS uk_gilt_yields (
    date DATE PRIMARY KEY,
    value NUMERIC
);
"""

def init_db():
    engine = get_engine()
    with engine.begin() as conn:
        conn.execute(text(DDL))

if __name__ == "__main__":
    init_db()
