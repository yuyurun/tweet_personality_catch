# coding : UTF-8

import settings
import tweepy

consumer_key    = settings.CK
consumer_secret = settings.CS
access_key      = settings.AK
access_secret   = settings.AS

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

tweets = api.user_timeline('@yuyurun', count=10)
for tweet in tweets:
    print(tweet.text, "/n")
