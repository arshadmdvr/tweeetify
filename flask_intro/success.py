import tweepy

#Add your credentials here
twitter_keys = {
        'consumer_key':        'EARO09bbaUcj8J55sBl0PFXeJ',
        'consumer_secret':     'WE1HdzsKqBAVk3Iy7cdRzWL9CzEiQiINj942RZPPFG51gqolK5',
        'access_token_key':    '1395946530805141504-6vjPcNvIJ228yQLkJXvc0aYY0FkjW0',
        'access_token_secret': '6Ci7yZpcxP7hXAOz5EDS8NQhi8pu493SQPrj1OLywnsOD'
    }

#Setup access to API
auth = tweepy.OAuthHandler(twitter_keys['consumer_key'], twitter_keys['consumer_secret'])
auth.set_access_token(twitter_keys['access_token_key'], twitter_keys['access_token_secret'])

api = tweepy.API(auth)

tweets = tweepy.Cursor(api.search,
              q="@tweeetify",
              include_entities="false").items(5)
tweets



for s in tweets:
    text= "@"+ s.in_reply_to_screen_name +" tweeted: "+ (api.get_status(s.in_reply_to_status_id)).text
    print(text)
    #print(api.get_user(s.in_reply_to_status_id))
    #api.send_direct_message(s.user.id,text)


#tweetss = api.get_status(tweet.in_reply_to_status_id)
#for tweet in tweetss:
#print(tweetss.text)

#for tweet in tweets:
    #print(tweet.text)    

#api.send_direct_message('987311315214589952', "Hoi hoi")