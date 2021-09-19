import tweepy
import json
import datetime

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

from fpl import *

with open('gameweek.txt') as file:
    data = json.load(file)

g = gameweeknum()
l = laddertweet()

l_list = data['tables']

latestweek = l.split('\n')

l_list[str(g)] = latestweek

dic = {"latest gameweek":g, "tables":l_list}



if data['latest gameweek'] == g:
    #print("Twitter already up to date")
    pass

else:
    g += '\n\n'
    message = 'Gameweek: '+ g + l   
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    api.update_status(message)

    #print("Tweeted successfully " + g)
    with open('gameweek.txt', 'w') as json_file:
            json.dump(dic, json_file, indent=4)
    
