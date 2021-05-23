
import tweepy

#Add your credentials here
twitter_keys = {
        'consumer_key':        'N2hwaNjoKuoFoYPgWsRh2JUMW',
        'consumer_secret':     'LGK4qeeUY6XEQ0ZJxzz56iVHhv7ydP4OfEJqSo0gPIT3OU9HnT',
        'access_token_key':    '1394666035379281922-5pohDKGgwd06PXtJ65pvIisAiSgDM8',
        'access_token_secret': 'EKif76ASlPDNkqqweXFQENCn1En2hVOzggdMHEyQvbfWZ'
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

for tweet in tweets:
    print(tweet.user.id)
   # print(f"Liking tweet {tweet.id} of {tweet.author.name}")
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
#for tweet in tweets:
    #print(api.get_status(tweet.in_reply_to_status_id).text,"\n")
    #print(tweet.text)
#for tweet in tweets:
    #print(api.get_status(tweet.in_reply_to_status_id).id,"\n")
    
#recipient_id = "2707179805"  # ID of the user
#api.send_direct_message(recipient_id, "Hoi hoi")

# fetching the user
#user = api.get_user(id)
  
# fetching the screen name
#screen_name = user.screen_name
  
#print("The screen name of the user is : " + screen_name)