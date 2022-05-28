import tweepy
import tkinter as tk
from datetime import datetime, date, time, timezone
import os
from dotenv import load_dotenv
import requests
from ctypes import windll
import datetime
import json

load_dotenv()

consumer_key = os.getenv('consumer_key')
consumer_secret = os.getenv('consumer_secret')
access_token = os.getenv('access_token')
access_secret = os.getenv('access_secret')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

root = tk.Tk()

counter = 0
has_tweeted = False
font = "Terminal"

def tK_init():
    root.geometry('600x600')
    root.title('Tweepy Bot')
    welcome_message = tk.Label(root, text="Welcome to Tweepy Bot.", font = (font, 25))
    welcome_message.pack()
    message = tk.Label(root, text="Your connected Twitter account will now post\n a random quote every hour.",
                       font=(font, 14))
    message.pack(ipady=50)
    button = tk.Button(root, text="Stop Bot", command=root.destroy, font=(font, 13))
    button.pack(ipady=50, ipadx=50, expand=True)
    try:
        windll.shcore.SetProcessDpiAwareness(1)
    finally:
        root.after(2000, task)
        root.mainloop()


def get_random_quote():
    len_response = 1000
    quoteText = ''
    quoteAuthor = ''
    while len_response > 280:
        response = requests.get("https://quote-garden.herokuapp.com/api/v3/quotes/random")
        if response.status_code == 200:
            json_data = response.json()
            data = json_data['data']
            quoteText = str(data[0]['quoteText'])
            quoteAuthor = str(data[0]['quoteAuthor'])
            len_response = len(quoteText)
    return quoteText, quoteAuthor


def tweet_quote():
    quote = get_random_quote()[0]
    author = get_random_quote()[1]
    tweet = '"' + quote + '" ' + "- " + author
    api.update_status(tweet)
    print("Tweet sent successfully.")


def task():
    global counter
    global has_tweeted
    if datetime.datetime.now().minute == 5 and not has_tweeted:
        has_tweeted = True
        tweet_quote()
    if datetime.datetime.now().minute == 6 and has_tweeted:
        has_tweeted = False
    print("Refreshing. . . " + str(counter))
    counter += 1
    root.after(10000, task)


if __name__ == '__main__':

    tK_init()

