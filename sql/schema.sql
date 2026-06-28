CREATE TABLE fact_nav (
    amfi_code INTEGER,
    date TEXT,
    nav REAL
);

CREATE TABLE fact_transactions (
    investor_id TEXT,
    transaction_date TEXT,
    amfi_code INTEGER,
    transaction_type TEXT,
    amount_inr INTEGER,
    state TEXT,
    city TEXT
);

CREATE TABLE fact_performance (
    amfi_code INTEGER,
    scheme_name TEXT,
    return_1yr_pct REAL,
    expense_ratio_pct REAL
);
