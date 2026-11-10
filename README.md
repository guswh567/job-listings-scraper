# Job Listings Scraper

## Project Description

This project is a Python web scraper designed to help programmers find remote job opportunities worldwide.

It automatically collects job listings from We Work Remotely and filters opportunities labeled "Anywhere in the World."

The program extracts job titles, company names, locations, and job URLs, then saves the results to a CSV file.

The goal is to reduce the time spent manually searching for remote jobs and eventually allow users to find opportunities based on their preferred criteria.


## Features

- Collects remote job listings from We Work Remotely.
- Filters jobs labeled "Anywhere in the World."
- Extracts job titles, company names, locations, and job URLs.
- Saves the collected data to a CSV file.


## Installation

Install the required Python packages:

```bash
pip install requests beautifulsoup4
```


## Usage

Run the scraper using the following command:

```bash
python scraper.py
```

The program collects remote job listings and saves the results to `jobs.csv`.


## Output

The program automatically generates a `jobs.csv` file containing the collected job listings.

Each job listing includes:

- Job title
- Company name
- Location
- Job URL