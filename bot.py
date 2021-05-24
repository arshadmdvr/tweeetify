#!/usr/bin/env python
# tweepy-bots/bots/followfollowers.py
import tweepy
import logging
import time
import config

#Setup access to API
auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token_key, config.access_token_secret)
    
api = tweepy.API(auth, wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)


#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, s):
        api.send_direct_message(s.user.id,(api.get_status(s.in_reply_to_status_id)).user.name +" ("+ "@"+ s.in_reply_to_screen_name +") "+ "tweeted: "+ (api.get_status(s.in_reply_to_status_id)).text
) 

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(track=['@sendmett'])