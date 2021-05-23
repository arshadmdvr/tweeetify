# tweepy-bots/bots/config.py
import tweepy
import logging
import os

logger = logging.getLogger()

def create_api():
    consumer_key = 'EARO09bbaUcj8J55sBl0PFXeJ'
    consumer_secret = 'WE1HdzsKqBAVk3Iy7cdRzWL9CzEiQiINj942RZPPFG51gqolK5',
    access_token = '1395946530805141504-6vjPcNvIJ228yQLkJXvc0aYY0FkjW0'
    access_token_secret = '6Ci7yZpcxP7hXAOz5EDS8NQhi8pu493SQPrj1OLywnsOD'
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api