# 🕸️ Coffee Quality Data Scraping

This folder contains all code and results from scraping coffee quality data from the **Coffee Quality Institute (CQI)** database.

The scraping process is isolated from the rest of the project using its own Python virtual environment (`.venv`), dependencies, and scripts.

> **Note:** This scraper requires login credentials for the CQI website. Do not commit your credentials to the repository.

---

## 📁 Folder Structure

scraped_dataset/

├── .venv/ # Virtual environment used for the scraper

├── requirements.txt # Libraries needed for scraping

├── scraper/

│ ├── scraper_bot.py # Main Selenium+BeautifulSoup scraper

│ ├── moving_csv.py # Moves generated CSVs into raw_data/

│ ├── process_tables_f.py # Merges table CSVs into a combined dataset

│ ├── raw_data/ # Folder where raw scraped CSVs are stored

│ └── df_1_arabica.csv # Combined dataset from scraping (pre-cleaned)


---

## 🔐 Environment Setup

To prepare the scraping environment:

1. Navigate to the `scraped_dataset/` folder.
2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate      # Windows
   source .venv/bin/activate     # macOS/Linux
   ```
   
Install dependencies:
   ```bash
   pip install -r requirements.txt
```

## 🚀 Running the Scraper
Once the environment is active, run:
```bash
python scraper/scraper_bot.py
```


What this does:

Logs into the CQI website

Navigates to the Arabica Coffees section

Iterates through available pages

Opens each coffee detail page

Extracts all HTML tables

Saves them as CSV files (one file per table, per coffee)

Each output CSV is named like:
   coffee_<id>_table_<index>.csv

## 📦 Organizing Raw Data
After scraping finishes, run:

```bash
python scraper/moving_csv.py
```
This will:

   Create the raw_data/ folder (if it doesn’t exist)
   
   Move all CSV files starting with coffee_ into it
   
Now your directory looks like:

scraped_dataset/scraper/raw_data/

## 🧠 Merging Into a Combined Dataset
Run the table-processing script:
```bash
python scraper/process_tables_f.py
```
This will:

   Read all raw coffee CSV tables from raw_data/
   
   Merge them by coffee ID into one complete record
   
   Skip incomplete or malformed entries
   
Resulting file:

scraped_dataset/scraper/df_1_arabica.csv

This is a combined dataset ready for cleaning and analysis.

## 📊 Current Dataset Summary

Dataset contains ~229 coffee entries

Each entry has ~40 features

Reflects the current contents of the CQI database

Matches the number of records visible manually on the site

Larger datasets found online (1300+) are historical exports, not current site data.

## ❗Important Notes

Login credentials are required only for scraping and should be stored securely (e.g., environment variables).

Avoid committing .venv and credentials to version control.

This folder only contains scraping logic & results — see the main project folder for modeling and analysis.
