# Day 2 Summary: Data Cleaning + SQLite Database

## Objective
The goal of Day 2 was to clean raw datasets and build a structured SQLite database for analysis.
## Data Cleaning
### NAV History Data
- Converted date column to datetime format
- Sorted data by fund code and date
- Removed duplicates
- Handled missing NAV values

### Investor Transactions
- Standardized transaction types (SIP, Lumpsum, Redemption)
- Removed invalid records
- Converted dates to proper format
- Ensured amount values are valid

### Scheme Performance
- Converted numeric columns properly
- Handled missing values
- Filtered invalid expense ratio values
## Processed Data
All cleaned datasets were saved in:
- `data/processed/`
## SQLite Database
- Created SQLite database: `bluestock_mf.db`
- Loaded cleaned data into tables:
  - fact_nav
  - fact_transactions
  - fact_performance
## Data Pipeline
Raw Data → Cleaning → Processed Data → SQLite Database
## Outcome
- Cleaned datasets ready for analysis
- Database created successfully
- Data loaded into SQL tables
- Project ready for SQL queries and analytics