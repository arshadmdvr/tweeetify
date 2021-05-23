import logging
import tweepy
import time
import os
logger = logging.getLogger()

def create_api():
    consumer_key = "EARO09bbaUcj8J55sBl0PFXeJ"
    consumer_secret = "WE1HdzsKqBAVk3Iy7cdRzWL9CzEiQiINj942RZPPFG51gqolK5"
    access_token = "1395946530805141504-6vjPcNvIJ228yQLkJXvc0aYY0FkjW0"
    access_token_secret = "6Ci7yZpcxP7hXAOz5EDS8NQhi8pu493SQPrj1OLywnsOD"

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


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def check_mentions(api, keywords, since_id):
    logger.info("Retrieving mentions")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline,
        since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id is not None:
            continue
        if any(keyword in tweet.text.lower() for keyword in keywords):
            logger.info(f"Answering to {tweet.user.name}")

            if not tweet.user.following:
                tweet.user.follow()

            api.update_status(
                status="Please reach us via DM",
                in_reply_to_status_id=tweet.id,
            )
    return new_since_id

def main():
    api = create_api()
    since_id = 1
    while True:
        since_id = check_mentions(api,["help", "support"], since_id)
        logger.info("Waiting...")
        time.sleep(60)

if __name__ == "__main__":
    main()
