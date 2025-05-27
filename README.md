# 🛒 Market Basket Analysis Using FP-Growth Algorithm

This project performs Market Basket Analysis using the **FP-Growth algorithm**. It analyzes transaction data from a CSV file and generates frequent itemsets and association rules to uncover purchasing patterns.

---

## 📌 Features

- Load transactional data from a CSV file
- One-hot encode items using `mlxtend`'s `TransactionEncoder`
- Apply FP-Growth algorithm to find frequent itemsets
- Generate association rules (support, confidence, lift)
- Customizable support and confidence thresholds
- Clean, readable output for easy interpretation

---

## 🧠 What is Market Basket Analysis?

Market Basket Analysis (MBA) is a data mining technique used to uncover associations between items purchased together. It helps businesses with:

- Product placement strategies
- Cross-selling opportunities
- Bundle offers and promotions

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/market-basket-fp-growth.git
cd market-basket-fp-growth
```
### 2. Install Dependencies
pip install pandas mlxtend

### 3. Transactional data
refer this link to download the csv file https://www.kaggle.com/datasets/aslanahmedov/market-basket-analysis?resource=download

## How to Run
### Run this analysis script:
```python3
python3 market_basket_fp_growth.py
```
