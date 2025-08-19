# Personal Finance Tracker

A simple command-line tool in Python to track your daily income and expenses.  
All records are saved in a CSV file for easy access and analysis.

---

## Features

- Add new transactions (date, amount, category, description)
- Automatically creates the CSV file on first run
- Clean modular code with input validation (`data_entry.py`)

---

## Requirements

- Python 3.x
- `pandas` library

Install dependencies:
```bash
pip install pandas

---

## Files

- main.py – core logic to initialize and add entries
- data_entry.py – handles user input
- finance_data.csv – stores your data

