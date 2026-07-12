# Python-Modules-CSV

A Python project demonstrating core built-in modules and file handling techniques, including data extraction and filtering from real-world datasets.

## Overview

This repository showcases practical implementation of Python's standard library modules alongside CSV file processing. It covers mathematical operations, randomization, date/time handling, and structured data filtering across multiple datasets.

## Contents

### Modules.py
Demonstrates the use of three core Python modules:
- **Math Module** — square roots, exponentiation, constants (π), and geometric calculations
- **Random Module** — random number generation, OTP creation, and random selection from a list
- **Date & Time Module** — retrieving current date/time and simulating time delays

### CSV File Handling
Each dataset includes a dedicated Python script that reads the CSV file and applies multiple filtering conditions:

| Script | Dataset | Description |
|--------|---------|--------------|
| `arizona.py` | `arizona.csv.7z` | Filters records by incident type, ethnicity, and year |
| `arkansas.py` | `arkansas.csv` | Filters records by race, gender, status, and age |
| `police.py` | `police.csv` | Filters records by gender, violation type, race, and outcome |
| `practice.py` | `practice.csv` | Filters records by category, year, income type, and value threshold |

## How to Run

1. Clone the repository
```bash
   git clone https://github.com/maryam-hamid-sa/Python-Modules-CSV.git
```
2. Navigate to the project folder
```bash
   cd Python-Modules-CSV
```
3. Update the file path inside each script to match your local CSV location
4. Run any script using Python
```bash
   python arizona.py
```

**Note:** `arizona.csv.7z` is compressed due to file size. Extract it using 7-Zip or WinRAR before running `arizona.py`.

## Technologies Used
- Python 3
- Built-in `csv` module
- Built-in `math`, `random`, and `datetime` modules

## Author
**Maryam Hamid**
