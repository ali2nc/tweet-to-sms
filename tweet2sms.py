# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 19:41:43 2023

@author: Ali
"""

import requests
import tweepy
import time

# Twitter API connection
consumer_key = 'consumer_key'
consumer_secret = 'consumer_secret'
access_token = 'access_token'
access_token_secret = 'access_token_secret'

# Nexmo & Vonage API connection
api_key = "api_key"
api_secret = "api_secret"

# Twitter username
pusholder_screen_name = "username"

# SMS
to_number = "phone_number"

# latest tweet
last_tweet_id = None

def send_sms(message):
    response = requests.post(
        "https://rest.nexmo.com/sms/json",
        headers={
            "Content-Type": "application/json"
        },
        json={
            "api_key": api_key,
            "api_secret": api_secret,
            "to": to_number,
            "from": "Nexmo",
            "text": message
        }
    )
    response_json = response.json()
    if response_json["messages"][0]["status"] == "0":
        print("SMS sent successfully!")
    else:
        print("Failed to send SMS.")

# get latest tweet via Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

while True:
    pusholder_tweets = api.user_timeline(screen_name=pusholder_screen_name, count=1)

    for tweet in pusholder_tweets:
        if last_tweet_id is None or last_tweet_id != tweet.id:
            send_sms(tweet.text)
            last_tweet_id = tweet.id

    time.sleep(600) # wait 10 mins
