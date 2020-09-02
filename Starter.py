import self as self
import tweepy
from FinalTweet import TweetFinal
Access_token = ''
Access_token_secret = ''

Bearer_token = ''

CONSUMER_KEY = ''
CONSUMER_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(Access_token, Access_token_secret)
api = tweepy.API(auth)

#final_tweet return will return a poem from assocaiated JSON file
TweetData = TweetFinal.final_tweet(self)

try:
    api.verify_credentials()
    print("Authentication OK")
    
    #Tweet
    api.update_status(TweetData)
except:
    print("Error during authentication")
