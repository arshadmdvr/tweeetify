import tweepy
import logging
import time
import os

consumer_key=os.getenv('ck')
consumer_secret = os.getenv('cs')
access_token = os.getenv('atk')
access_token_secret = os.getenv('ats')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, s):
        api.send_direct_message(s.user.id,(api.get_status(s.in_reply_to_status_id)).user.name +" ("+ "@"+ s.in_reply_to_screen_name +") "+ "tweeted: "+ (api.get_status(s.in_reply_to_status_id, tweet_mode="extended")).full_text) 

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(track=['@sendmett'])
