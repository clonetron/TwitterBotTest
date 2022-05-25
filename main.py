import tweepy
import tkinter as tk
from datetime import datetime, date, time, timezone
import os
from dotenv import load_dotenv
import requests
from ctypes import windll

load_dotenv()

consumer_key = os.getenv('consumer_key')
consumer_secret = os.getenv('consumer_secret')
access_token = os.getenv('access_token')
access_secret = os.getenv('access_secret')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)


def hello():
    print("helloWorld")


def tK_init():
    root = tk.Tk()
    root.geometry('500x500')
    root.title('Tweepy Bot')

    message = tk.Label(root, text="Welcome to Tweepy Bot. Please press the button to send a random tweet.")
    message.pack()

    button = tk.Button(root, text="Send Tweet", command=tweet_quote)
    button.pack(ipady=50, ipadx=50, expand=True)

    try:
        from ctypes import windll

        windll.shcore.SetProcessDpiAwareness(1)
    finally:
        root.mainloop()

def get_random_quote():
    len_response = 1000
    quoteText = ''
    while len_response > 280:
        response = requests.get("https://quote-garden.herokuapp.com/api/v3/quotes/random")
        if response.status_code == 200:
            json_data = response.json()
            data = json_data['data']
            quoteText = str(data[0]['quoteText'])
            len_response = len(quoteText)
    return quoteText


def tweet_quote():
    quote = get_random_quote()
    tweet = '"' + quote + '"'
    api.update_status(tweet)
    print("Tweet sent successfully.")

if __name__ == '__main__':

    tK_init()


