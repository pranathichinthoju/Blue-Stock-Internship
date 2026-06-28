import os
import requests
import pandas as pd

# Create folder if it doesn't exist
os.makedirs("data/raw", exist_ok=True)

# Scheme codes
schemes = {
    "119551": "sbi_bluechip",
    "120503": "icici_bluechip",
    "118632": "nippon_large_cap",
    "119092": "axis_bluechip",
    "120841": "kotak_bluechip"
}

for code, name in schemes.items():
    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    print(f"\nFetching {name}")
    print("Scheme:", data["meta"]["scheme_name"])

    df = pd.DataFrame(data["data"])

    filename = f"data/raw/{name}.csv"
    df.to_csv(filename, index=False)

    print(f"Saved as {filename}")