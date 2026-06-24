# Convexity Sensitivity AI Agent

## Project Overview

This project focuses on developing an AI-powered bond risk analytics platform for fixed-income portfolio analysis.

The solution will combine bond pricing, duration and convexity analytics, yield curve modeling, Monte Carlo simulations, machine learning models, and Power BI dashboards to evaluate portfolio sensitivity under changing market conditions.

---

## Project Objectives

- Analyze bond portfolio interest-rate risk
- Calculate Duration, Convexity, and DV01
- Perform Yield Curve Analysis
- Run Monte Carlo Simulations
- Estimate Value-at-Risk (VaR) and CVaR
- Develop Machine Learning Models for bond price prediction
- Create Interactive Power BI Dashboards

---

## Day 1 Progress

### Topics Covered

- Bond Fundamentals
- Bond Pricing
- Yield to Maturity (YTM)
- Macaulay Duration
- Modified Duration
- Convexity
- DV01 (Dollar Value of One Basis Point)

### Key Learnings

- Bond prices move inversely to interest rates.
- Duration measures bond price sensitivity to interest-rate changes.
- Convexity improves duration-based price estimates.
- DV01 measures the monetary impact of a 1 basis-point change in yield.

---

## Project Roadmap

### Phase 1: Bond Analytics
- Bond Pricing
- Duration
- Convexity
- DV01

### Phase 2: Yield Curve Analytics
- Yield Curve Construction
- Nelson-Siegel Model

### Phase 3: Risk Analytics
- Stress Testing
- Scenario Analysis
- Monte Carlo Simulation

### Phase 4: Machine Learning
- Random Forest
- XGBoost
- Neural Networks

### Phase 5: Dashboard Development
- Power BI
- DAX Measures
- Risk Visualization

---



## Tools & Technologies

- Python
- NumPy
- Pandas
- SciPy
- Power BI
- DAX
- Machine Learning
- Monte Carlo Simulation

---

## Author

**Renu Shokeen**

Data Analytics | Risk Analytics | Machine Learning




## Day 2 Progress

### Completed

- Imported bond portfolio dataset (44 columns)
- Built portfolio risk analytics module
- Calculated:
  - Portfolio Duration
  - Portfolio Convexity
  - Portfolio Yield
  - Total Market Value
- Created exploratory data analysis notebook
- Visualized market value distribution by credit rating

### Dataset Features

- Duration Metrics
- Convexity Metrics
- DV01
- OAS Spread
- Z Spread
- Interest Rate Sensitivity
- Portfolio Weights
- Market Values


## Key Findings

### Credit Rating Analysis
- Sovereign bonds represent the largest portion of portfolio market value.
- Majority of investments are concentrated in highly rated securities (SOV and AAA).
- Portfolio exhibits low credit risk exposure.

### Duration vs Convexity Analysis
- Strong positive relationship between duration and convexity.
- Long-duration bonds are more sensitive to interest rate changes.
- Portfolio interest-rate risk is concentrated in high-duration securities.



# Portfolio Risk Findings

- Government sector dominates portfolio allocation.
- Portfolio duration indicates moderate interest-rate sensitivity.
- Convexity provides positive protection against large rate moves.
- Risk is concentrated in a small number of sectors.
- Portfolio yield remains above 7%.


# Yield Curve Findings

- Yield curve is generally upward sloping.
- Long-term rates are higher than short-term rates.
- Indicates normal market conditions.
- Forward rates suggest expectations of future interest rates.
- Zero rates remain close to observed market yields.