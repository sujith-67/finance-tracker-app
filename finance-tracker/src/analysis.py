import pandas as pd
import sqlite3

DB_PATH = "data/finance.db"

def load_data():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql("SELECT * FROM transactions", conn)
    conn.close()

    if not df.empty:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")

    return df

def category_summary(df):
    return df.groupby("category")["amount"].sum()

def monthly_summary(df):
    return df.groupby(df["date"].dt.month)["amount"].sum()