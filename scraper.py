import requests
import csv
from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com"
url = base_url + "/remote-full-stack-programming-jobs"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

jobs = soup.find_all("li", class_="new-listing-container")

job_list = []

for job in jobs:
    company = job.find(
        "p",
        class_="new-listing__company-name"
    )

    title = job.find(
        "span",
        class_="new-listing__header__title__text"
    )

    links = job.find_all("a")

    categories = job.find_all(
        "p",
        class_="new-listing__categories__category"
    )

    location = categories[-1]

    title_text = title.text.strip()
    company_text = company.text.strip()
    location_text = location.text.strip()

    if location_text == "Anywhere in the World":
        job_url = base_url + links[-1]["href"]

        job_data = {
            "title": title_text,
            "company": company_text,
            "location": location_text,
            "url": job_url
        }

        job_list.append(job_data)

        print("직무:", job_data["title"])
        print("회사:", job_data["company"])
        print("지역:", job_data["location"])
        print("링크:", job_data["url"])
        print("--------------------------------")

with open("jobs.csv", "w", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["title", "company", "location", "url"]
    )

    writer.writeheader()
    writer.writerows(job_list)