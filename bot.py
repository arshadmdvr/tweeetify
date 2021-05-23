#!/usr/bin/env python
# tweepy-bots/bots/followfollowers.py

import tweepy
import logging
import time

twitter_keys = {
        'consumer_key':        'EARO09bbaUcj8J55sBl0PFXeJ',
        'consumer_secret':     'WE1HdzsKqBAVk3Iy7cdRzWL9CzEiQiINj942RZPPFG51gqolK5',
        'access_token_key':    '1395946530805141504-6vjPcNvIJ228yQLkJXvc0aYY0FkjW0',
        'access_token_secret': '6Ci7yZpcxP7hXAOz5EDS8NQhi8pu493SQPrj1OLywnsOD'
    }

#Setup access to API
auth = tweepy.OAuthHandler(twitter_keys['consumer_key'], twitter_keys['consumer_secret'])
auth.set_access_token(twitter_keys['access_token_key'], twitter_keys['access_token_secret'])
    
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