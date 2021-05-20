
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

# Define the search term and the date_since date as variables
search_words = "@tweeetify"
date_since = "2021-05-01"

# Collect tweets
tweets = tweepy.Cursor(api.search,
              q=search_words,
              lang="en",
              id="tweeetify",
              include_entities="false").items(5)
tweets

#users_locs = [['tweeetify'] for tweet in tweets]
#users_locs

# Iterate and print tweets
#for tweet in tweets:
#print(tweet.in_reply_to_status_id)
#print(tweet)
#tweetss = api.get_status("1395041849438519296")
#for tweet in tweetss:
#print(tweetss.text)



#Make call on home timeline, print each tweets text
#public_tweets = api.home_timeline()
for tweet in tweets:
    print(api.get_status(tweet.in_reply_to_status_id).text,"\n")
    #print(tweet.text)
