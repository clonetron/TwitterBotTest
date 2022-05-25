import tweepy
import tkinter
from datetime import datetime, date, time, timezone
import os
from dotenv import load_dotenv

load_dotenv()

consumer_key = os.getenv('consumer_key')
consumer_secret = os.getenv('consumer_secret')
access_token = os.getenv('access_token')
access_secret = os.getenv('access_secret')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)


if __name__ == '__main__':
    current_time = datetime.now().time()
    print(current_time)

    api.update_status("Posting now, at " + str(current_time))
