# TTDS Assignment 1 — Faculty Web Scraper

A web scraper that extracts faculty profile information (name, designation, email, research interests) from a university Faculty of IT & Computer Science website and exports the data to CSV.

## Use Case

Data collection for academic research, building faculty directories, or learning web scraping fundamentals. Demonstrates the full scraping workflow: HTTP requests → HTML parsing → structured data extraction → CSV export.

## Features

- Fetches the faculty listing page and identifies all faculty members by designation
- Filters by academic rank (Professor, Associate Professor, Assistant Professor)
- Visits each faculty member's individual profile page to extract detailed info
- Exports structured results to CSV

## Tech Stack

| Layer | Tools |
|---|---|
| Language | Python 3.7+ |
| HTTP | requests |
| HTML Parsing | BeautifulSoup4 |
| Data Export | pandas |

## Prerequisites

- Python 3.7 or higher
- Internet connection (scraper fetches live web pages)

## Installation

```bash
pip install requests beautifulsoup4 pandas
```

## Running

```bash
python scrapper.py
```

Output is saved to `faculty_info.csv` in the same directory.

## How It Works

1. Fetches the faculty listing page from the university website
2. Finds all `<h4>` tags matching faculty designations (Professor, Associate/Assistant Professor)
3. For each relevant faculty member, visits their individual profile page
4. Extracts: **name**, **designation**, **email**, **research interests**
5. Saves all records to `faculty_info.csv`

## Project Structure

```
├── scrapper.py         # Web scraper — fetches and parses faculty profiles (run this)
├── faculty_info.csv    # Scraped output data (included as sample)
└── documentation.docx  # Assignment documentation
```

## Output & Results

`faculty_info.csv` columns:

| Column | Description |
|---|---|
| Name | Faculty member's full name |
| Designation | Academic rank (Professor, Associate/Assistant Professor) |
| Email | Contact email address |
| Research Interests | Listed research areas from profile page |

## Notes

- The scraper targets a specific university website — if the site's HTML structure changes, the CSS selectors in `scrapper.py` will need updating
- Scraping may fail if the university website is unreachable or rate-limits requests
- `faculty_info.csv` in the repo is a sample output from a previous run
