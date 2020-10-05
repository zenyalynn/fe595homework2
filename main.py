#Zenya Koprowski
#FE 595 Homework 2
#received help from this website: https://hackernoon.com/how-to-build-a-web-scraper-with-python-step-by-step-guide-jxkp3yum

import requests
import os
import pandas as pd
from requests import get
from bs4 import BeautifulSoup

def check_url(url):
    results = requests.get(url)
    if results.status_code == 200:
        return True
    else:
        return False

def extract_info(url):
    cname = [] #list to store the name of the companies
    cpurpose = [] #list to store the purpose of the companies
    i = 0
    while i < 50:

        results = requests.get(url)
        soup = BeautifulSoup(results.text, "html.parser")

        try:  # If the name or purpose is not found on the page, it will throw an error
            name = soup(text=lambda t: "Name" in t)[0][6:]
            purpose = soup(text=lambda t: "Purpose" in t)[0][9:]
        except:
            continue

        # Here we append the values to the lists
        cname.append(name)
        cpurpose.append(purpose)

        i += 1

    clist = pd.DataFrame({
        'Company Name': cname,
        'Company Purpose': cpurpose,
    })

    return clist

def main():
    url = "http://3.95.249.159:8000/random_company"
    if check_url(url):
        clist = extract_info(url)
        clist.to_csv('finalcompanyinfo.csv')
    else:
        print("URL did not work, please try again.")
        return None

if __name__ == "__main__":
    main()
