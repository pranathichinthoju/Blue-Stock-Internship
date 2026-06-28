import pandas as pd
from sqlalchemy import create_engine

# Create SQLite database
engine = create_engine("sqlite:///bluestock_mf.db")

print("Database created...")

# -----------------------------
# LOAD CLEANED DATA
# -----------------------------

nav = pd.read_csv("data/processed/nav_history_cleaned.csv")
txn = pd.read_csv("data/processed/investor_transactions_cleaned.csv")
perf = pd.read_csv("data/processed/scheme_performance_cleaned.csv")

# -----------------------------
# LOAD INTO SQLITE TABLES
# -----------------------------

nav.to_sql("fact_nav", engine, if_exists="replace", index=False)
print("Loaded fact_nav")

txn.to_sql("fact_transactions", engine, if_exists="replace", index=False)
print("Loaded fact_transactions")

perf.to_sql("fact_performance", engine, if_exists="replace", index=False)
print("Loaded fact_performance")

print("All tables loaded successfully!")