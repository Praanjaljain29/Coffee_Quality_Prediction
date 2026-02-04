# ☕ Coffee Quality Data Scraping

This folder contains all code and results used to scrape coffee quality data from the **Coffee Quality Institute (CQI)** official database.

The purpose of this scraping pipeline is to collect raw coffee quality tables and prepare them for blending into a clean dataset suitable for analysis and machine learning.

---

## 📁 Folder Structure

scraped_dataset/
├── .venv/ # Python virtual environment for the scraper
├── requirements.txt # Dependencies for the scraping environment
└── scraper/
├── scraper_bot.py # Main scraper script
├── moving_csv.py # Moves generated CSV files to raw_data/
├── process_tables_f.py # Combines raw table CSVs into a merged dataset
├── raw_data/ # Folder with raw coffee table CSV files
└── df_1_arabica.csv # Merged dataset from the raw CSV files


---

## 📌 What This Scraper Does

The CQI database requires a logged-in user to view detailed coffee reports. This script:

1. Opens the CQI login page
2. Submits login credentials
3. Navigates to the *Arabica Coffees* list
4. Iterates through all available pages
5. Clicks into each coffee’s detail page
6. Extracts every HTML table found there
7. Saves each table as a separate CSV

Each coffee generates multiple CSV files named:

coffee_<coffee_id>table<table_index>.csv


All raw CSV files are stored in the `raw_data/` folder.

---

## 🛠️ Environment Setup

To configure the scraping environment:

```bash
cd scraped_dataset

# create virtual environment
python -m venv .venv

# activate environment
.\.venv\Scripts\activate     # Windows
source .venv/bin/activate    # Mac/Linux

# install dependencies
pip install -r requirements.txt
🚀 Running the Scraper
Once the environment is set up:

python scraper/scraper_bot.py
After the run completes, you will see many CSV files in the scraper/ directory.

📦 Organizing Raw Data
To organize the raw CSV files into raw_data/:

python scraper/moving_csv.py
This moves all files beginning with coffee_ into that folder.

📊 Combining Into a Dataset
To merge the raw CSV tables into a single dataset:

python scraper/process_tables_f.py
This generates:

df_1_arabica.csv
This file has:

~229 coffee entries

~40 columns

One row per coffee

🧠 Notes & Limitations
✔ Only Arabica coffees were scraped
✔ The number of entries (~229) matches the current available data on the site
✔ Larger datasets found online are historical and may not reflect the current database

IMPORTANT
⚠ Do not commit your login credentials to GitHub.

Credentials are required for scraping but should be stored securely (e.g., using .env or environment variables) and not in this repository.

🧾 Attribution
Data was scraped from the official Coffee Quality Institute database:
https://database.coffeeinstitute.org


---

## 📌 Where to Add It

👉 Create this file at:

scraped_dataset/README.md
