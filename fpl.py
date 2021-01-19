import requests
import json
import numpy as np
import pandas as pd
import datetime



link = "https://fantasy.premierleague.com/api/leagues-h2h/1416616/standings/#/"
response = requests.get(link)

data = json.loads(response.text)

def laddertweet():
    tweet = ""
    position = ""
    for i in data:
        if 'results' in data[i]:
            if len(data[i]['results']) > 1:
                for j in data[i]['results']:
                    if j['rank'] > j['last_rank']:
                        position = "⬆️"
                    elif j['rank'] < j['last_rank']:
                        position = "⬇️"
                    entry = str(j['rank']) + '. ' + j['entry_name'] + ' - ' + str(j['total']) + position + '\n'
                    tweet += entry
    return tweet

def gameweeknum():
    num = 0
    for i in data:
        if 'results' in data[i]:
            if len(data[i]['results']) > 1:
                for j in data[i]['results']:
                    num = j['matches_played']
    num += 1
    return str(num)

    
#print('Gameweek: ' + gameweeknum())
#print(laddertweet())

