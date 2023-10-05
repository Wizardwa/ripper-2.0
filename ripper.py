#!/bin/python

import os
import requests
from bs4 import BeautifulSoup
from lxml import html
import re

#Animating splash-screen
splash = os.system("figlet Ripper | lolcat -a")

"""print('''
 ____  _                       
|  _ \(_)_ __  _ __   ___ _ __ 
| |_) | | '_ \| '_ \ / _ \ '__|
|  _ <| | |_) | |_) |  __/ |   
|_| \_\_| .__/| .__/ \___|_|   
        |_|   |_|              

	''')
"""

zulu_url = "https://www.zulubet.com/"
req = requests.get(zulu_url)
data_req = BeautifulSoup(req.text, 'html.parser')

#writing to a file 
req_file =  open('tips.html', 'w')
req_file.write(str(data_req))
req_file.close()

#creating match details
with open('tips.html', 'r', encoding='UTF8') as f:
        contents = f.read()
        soup = BeautifulSoup(contents, 'lxml')

match_details = soup.find_all('tr', bgcolor=('#EFEFEF','#FFFFFF'))
#print(type(match_details))
for match in match_details:
        matches = {}
        list_matches = match.find_all('a')
        match_links = open('match_links', 'a')
        match_links.write('\n')
        match_links.write(str(list_matches))
        match_links.close()

regex = os.system('./regex.sh')

with open('solo_match_links', 'r') as solo:
        solo_links = solo.read()
        solo_links_array = solo_links.split()

#match_count = os.system('cat solo_match_links | wc -l')
#first match details
#search = int(input("Enter the match index: "))

first_match = solo_links_array[0] #change the index to search for a game 
first_match_req = requests.get(first_match)
data_first_match = BeautifulSoup(first_match_req.text, 'html.parser')
avg_goal = data_first_match.find_all('table', bgcolor=("#C0C0C0"))

#home team
home_team = data_first_match.find_all('h3')[0]
title = str(home_team)
title = title.strip('<h3/>')
print('\n')
print(title)
games_played = data_first_match.find('div', class_='statbox')
games_played = data_first_match.find('tr', bgcolor="#f4f4f4")
print(f"games \t goals \t aver. goals")
games_played = str(games_played)
games_played = re.findall(r'<td align="center">(.*?)</td>', games_played)
games_played = ' \t  '.join(games_played)
print(games_played)
print('\n')

#away team
away_team = data_first_match.find_all('h3')[1]
title = str(away_team)
title = title.strip('<h3/>')
print(title)
games_played_2 = data_first_match.find_all('div', class_='statbox')[1]
games_played_2 = data_first_match.find_all('tr', bgcolor="#f4f4f4")[4]
print(f"games \t goals \t aver. goals")
games_played_2 = str(games_played_2)
games_played_2 = re.findall(r'<td align="center">(.*?)</td>', games_played_2)
games_played_2 = ' \t  '.join(games_played_2)
print(games_played_2)

#rm links
rm = os.system("rm solo_match_links match_links")


#all matches
"""all_matches = solo_links_array
for matches in all_matches:
        req_2 = requests.get(matches)
        data_all = BeautifulSoup(req_2.text, 'html.parser')
        links = data_all.find_all('tr', bgcolor=('#EFEFEF','#FFFFFF'))
        links = data_all.find('td', class_="prob2 prediction_full")
        print(links)
        print('\n')"""
