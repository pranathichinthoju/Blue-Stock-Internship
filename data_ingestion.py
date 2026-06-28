import os
import pandas as pd

# Folder containing CSV files
data_folder = "data/raw"

# Get all CSV files
csv_files = [f for f in os.listdir(data_folder) if f.endswith(".csv")]

print(f"Found {len(csv_files)} CSV files.\n")

for file in csv_files:
    file_path = os.path.join(data_folder, file)

    print("=" * 70)
    print(f"File: {file}")

    try:
        df = pd.read_csv(file_path)

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

    except Exception as e:
        print(f"Error reading {file}: {e}")

    print("\n")
    print("\n========== FUND MASTER ANALYSIS ==========\n")

fund_master = pd.read_csv("data/raw/01_fund_master.csv")

print("Unique Fund Houses:")
print(fund_master["fund_house"].unique())

print("\nUnique Categories:")
print(fund_master["category"].unique())

print("\nUnique Sub Categories:")
print(fund_master["sub_category"].unique())

print("\nUnique Risk Categories:")
print(fund_master["risk_category"].unique())
print("\n========== AMFI SCHEME CODE ==========\n")

print("Total Records:", len(fund_master))
print("Unique AMFI Codes:", fund_master["amfi_code"].nunique())

print("\nFirst 10 AMFI Codes:")
print(fund_master["amfi_code"].head(10))
print("\n========== AMFI CODE VALIDATION ==========\n")

# Load nav history
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

# Get unique AMFI codes
fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

# Find missing codes
missing_codes = fund_codes - nav_codes

if len(missing_codes) == 0:
    print("✅ All AMFI codes in fund_master exist in nav_history.")
else:
    print("❌ Missing AMFI Codes:")
    print(missing_codes)

print(f"\nTotal Fund Master Codes : {len(fund_codes)}")
print(f"Total NAV History Codes : {len(nav_codes)}")