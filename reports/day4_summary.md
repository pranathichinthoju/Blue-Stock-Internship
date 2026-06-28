# Day 4 Summary – Fund Performance Analytics
## Objective
The objective of Day 4 was to analyze the performance of mutual fund schemes using various financial metrics and risk-adjusted performance measures. The analysis focused on evaluating fund returns, risk, benchmark comparison, and ranking funds based on multiple performance indicators.

## Tasks Completed

### 1. Daily Return Calculation

* Calculated daily percentage returns for all mutual fund schemes using daily NAV data.
* Verified the return distribution to ensure data consistency and identify any abnormal values.

### 2. CAGR Analysis

* Computed Compound Annual Growth Rate (CAGR) for available investment periods (1-Year, 3-Year, and available historical data for 5-Year calculations).
* Generated a comparison table for all funds.

### 3. Sharpe Ratio

* Calculated the annualized Sharpe Ratio using a risk-free rate of **6.5%**.
* Ranked all funds based on risk-adjusted returns.

### 4. Sortino Ratio

* Computed the Sortino Ratio by considering only downside volatility.
* Compared fund performance using downside risk instead of total volatility.

### 5. Alpha and Beta

* Used **scipy.stats.linregress** to estimate Alpha and Beta by comparing fund returns with the Nifty 100 benchmark.
* Exported the results to **alpha_beta.csv**.

### 6. Maximum Drawdown Analysis

* Calculated the maximum drawdown for each mutual fund.
* Identified the dates corresponding to the worst drawdown observed during the analysis period.

### 7. Fund Scorecard

* Developed a composite Fund Score (0–100) using the following weighted metrics:

  * 30% – 3-Year Return Rank
  * 25% – Sharpe Ratio Rank
  * 20% – Alpha Rank
  * 15% – Expense Ratio Rank (Inverse)
  * 10% – Maximum Drawdown Rank (Inverse)
* Ranked all mutual funds based on the composite score.

### 8. Tracking Error

* Calculated tracking error by comparing fund returns with benchmark returns.
* Evaluated benchmark consistency for each scheme.

### 9. Benchmark Comparison

* Created a comparison chart of the top-performing funds against **Nifty 50** and **Nifty 100** over the recent three-year period.
* Exported the visualization as **benchmark_comparison.png**.

## Files Generated

* Performance_Analytics.ipynb
* fund_cagr.csv
* sharpe_ratio.csv
* sortino_ratio.csv
* alpha_beta.csv
* max_drawdown.csv
* max_drawdown_dates.csv
* tracking_error.csv
* fund_scorecard.csv
* benchmark_comparison.png

## Key Learnings

* Learned to calculate financial performance metrics using Python and Pandas.
* Applied risk-adjusted performance measures including Sharpe and Sortino Ratios.
* Performed benchmark analysis using regression techniques.
* Evaluated portfolio risk through Maximum Drawdown and Tracking Error.
* Built a comprehensive scoring model to rank mutual funds based on return, risk, and expense efficiency.

## Outcome

Successfully completed the Fund Performance Analytics module by implementing return analysis, risk metrics, benchmark comparison, fund ranking, and visualization. The generated outputs provide a comprehensive evaluation of mutual fund performance and are ready for use in subsequent project phases.
