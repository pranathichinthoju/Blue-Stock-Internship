import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

# Convert date
df["date"] = pd.to_datetime(df["date"])

# Sort
df = df.sort_values(["amfi_code", "date"])

# Remove duplicates
df = df.drop_duplicates()

# Ensure NAV > 0
df = df[df["nav"] > 0]

# Forward fill missing NAV per fund
df["nav"] = df.groupby("amfi_code")["nav"].ffill()

# Save cleaned file
df.to_csv("data/processed/nav_history_cleaned.csv", index=False)

print("nav_history cleaned")
df = pd.read_csv("data/raw/08_investor_transactions.csv")

# Standardize transaction types
df["transaction_type"] = df["transaction_type"].str.upper()

# Fix invalid values
df = df[df["transaction_type"].isin(["SIP", "LUMPSUM", "REDEMPTION"])]

# Validate amount
df = df[df["amount_inr"] > 0]

# Convert date
df["transaction_date"] = pd.to_datetime(df["transaction_date"])

# KYC validation
df = df[df["kyc_status"].isin(["Verified", "Pending"])]

df.to_csv("data/processed/investor_transactions_cleaned.csv", index=False)

print("transactions cleaned")
df = pd.read_csv("data/raw/07_scheme_performance.csv")

# Convert numeric columns
num_cols = [
    "return_1yr_pct", "return_3yr_pct", "return_5yr_pct",
    "expense_ratio_pct", "alpha", "beta"
]

for col in num_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Expense ratio check
df = df[(df["expense_ratio_pct"] >= 0.1) & (df["expense_ratio_pct"] <= 2.5)]

df.to_csv("data/processed/scheme_performance_cleaned.csv", index=False)

print("scheme performance cleaned")
