from __future__ import print_function
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import csv

# Scrape website
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome('C:/Users/Jim/Documents/Python Dash Intro/venv/Lib/site-packages/chromedriver/chromedriver.exe', options=options)
site = "https://en.wikipedia.org/wiki/2020_Summer_Olympics"
driver.get(site)

print("Complete") #to check if has scraped successfully
time.sleep(10)
page = driver.page_source
driver.quit()

soup = BeautifulSoup(page, 'html.parser')

text_list = []
for i in range(len(soup.find_all('a'))):
    text = soup.find_all('a')[i].get_text()
    text_list.append((text))

# print(text_list)

# Extract the countries
text_list_start = text_list.index('Afghanistan')
text_list_end = text_list.index('Zimbabwe') + 1
country_list = text_list[text_list_start:text_list_end]
# print(country_list)

# Headers
header = ['Team/NOC']

# Data rows
data_rows = [country_list[i:i+1] for i in range(0, len(country_list), 1)]
# print(data_rows)

with open('Tokyo_2020_Participants.csv', 'w', newline="") as f:
    write = csv.writer(f)

    write.writerow(header)
    write.writerows(data_rows)