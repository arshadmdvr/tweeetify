import tweepy

#Add your credentials here
twitter_keys = {
        'consumer_key':        'Vh6JtMJsrxBjflEj7oKZTCczF',
        'consumer_secret':     'g14pxJdUTtFLd9j0xcWvAXTQxG5dOYh3wcVeqWiucX6b27FzAq',
        'access_token_key':    '987311315214589952-aMGfX9OKVjbsxvyEdqfqDe6xB52d8ah',
        'access_token_secret': 'gLJ24ZJjQP2t39VWuT0bz3YVg7GkAF2TIToqmjYBgPVsz'
    }

#Setup access to API
auth = tweepy.OAuthHandler(twitter_keys['consumer_key'], twitter_keys['consumer_secret'])
auth.set_access_token(twitter_keys['access_token_key'], twitter_keys['access_token_secret'])

api = tweepy.API(auth)

search_words = "@tweeetify"
#Make call on home timeline, print each tweets text
public_tweets =tweepy.Cursor(api.search,
              q=search_words,
              lang="en",
              id="tweeetify").items(5)

for tweet in public_tweets:
    print(tweet.text)

import json 

#status = public_tweets[0]

#convert to string
#json_str = json.dumps(status._json)

#deserialise string into python object
#parsed = json.loads(json_str)

#print(json.dumps(parsed, indent=4, sort_keys=True))
