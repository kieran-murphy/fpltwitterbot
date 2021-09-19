import requests
import json
import datetime



link = "https://fantasy.premierleague.com/api/leagues-h2h/244990/standings/#/"
response = requests.get(link)

data = json.loads(response.text)


def gameweeknum():
    num = data['standings']['results'][0]['matches_played']
    return str(num)



def laddertweet():
    tweet = ""
    position = ""
    for i in data['standings']['results']:
        if i['rank'] > i['last_rank']:
            position = "⬆️"
        elif i['rank'] < i['last_rank']:
            position = "⬇️"
        entry = str(i['rank']) + '. ' + i['entry_name'] + ' - ' + str(i['total']) + position + '\n'
        tweet += entry
    return tweet




