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
TweetData = TweetFinal.final_tweet(self)
#print(TweetData)

api.update_status(TweetData)

try:
    api.verify_credentials()
    print("Authentication OK")

except:
    print("Error during authentication")
