#!/bin/python

import requests
import re
from bs4 import BeautifulSoup
import os
import pandas as pd

splash = os.system("figlet Ripper | lolcat -a")

zulu_url = "https://www.zulubet.com/"
req = requests.get(zulu_url)
soup = BeautifulSoup(req.text, 'lxml')
table = soup.select('table.content_table')
matches = soup.select('table.content_table')[0]

for things in matches:
    urls = things.find_all('a')
    file = open('links.txt','a')
    file.write('\n')
    file.write(str(urls))
    file.close()

with open('links.txt' , 'r') as links:
    for l in links:
        new_links = []
        new_links = str(l)
        pattern = r'href="([^"]+)"'
        regex_match = re.search(pattern, new_links)
        if regex_match:
            link = regex_match.group(1)
            file = open('urls.txt', 'a')
            file.write('\n')
            file.write(link)
            file.close()

url_list = []
with open('urls.txt', 'r') as f:
    for line in f:
        url_list.append(line.strip())
#print(url_list)
os.system('rm links.txt urls.txt')
count = len(url_list)
print(f'Total links {count}')
index = 1
while index <= count:
    bulk_urls = url_list[index]
    bulk_request = requests.get(url_list[index])
    bulk_data = BeautifulSoup(bulk_request.text, 'lxml')
    title = bulk_data.find('title').get_text()
    print(title, '\n')
    table = pd.read_html(bulk_urls)[5]
    table_2 = pd.read_html(bulk_urls)[9]
    file = open('AverageGoals.txt', 'a')
    file.write(str(title))
    file.write('\n')
    file.write(str(table))
    file.write(str(table_2))
    file.write('\n')
    file.close()
    table
    index += 1

"""single_match = url_list[1]
single_req = requests.get(single_match)
soup = BeautifulSoup(single_req.text, 'lxml')
table = pd.read_html(single_match)[5]
#home team
home_team = soup.find_all('h3')[0]
title = str(home_team)
title = title.strip('<h3/>')
print('\n')
print(title)
print(table)

#Away team 
single_match = url_list[1]
single_req = requests.get(single_match)
soup = BeautifulSoup(single_req.text, 'lxml')
table = pd.read_html(single_match)[9]
#home team
away_team = soup.find_all('h3')[1]
title = str(away_team)
title = title.strip('<h3/>')
print('\n')
print(title)
print(table)"""
