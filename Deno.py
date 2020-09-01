import self as self
import tweepy
from FinalTweet import TweetFinal
Access_token = '2515291648-kjyDSDUP2ZMFUP4grqhHB2k3knwX2Lv4bBTbjSS'
Access_token_secret = 'NF4M1mh2u2J28BueqNQiHXtdWijAedW8u2UUHUfo7mcks'

Bearer_token = 'AAAAAAAAAAAAAAAAAAAAAHmfGgEAAAAAWUmllG5Ds%2BJXqYuywpe4yEzrimw' \
               '%3DlJczyZlYlb1SntAnphZuLTgm9hjWzrPvDZWBu0XYotH8Q4ygRA'

CONSUMER_KEY = 'tkSxEEURnWFOlmB7Gejd0kpzY'
CONSUMER_SECRET = 'LjfTPsA5xm48AHkWPqS95RVuS7f3HEqi5b6ORjIlDhAMidgMoS'

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
