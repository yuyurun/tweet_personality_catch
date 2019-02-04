# coding : UTF-8

import settings
import tweepy
import argparse
import time

import get_tweets

 
def get_tweet_page_all(acountname, num):
  consumer_key    = settings.CK
  consumer_secret = settings.CS
  access_key      = settings.AK
  access_secret   = settings.AS

  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_key, access_secret)
  api = tweepy.API(auth)

  #pages = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
  pages = [1,2,3,4,5]
  """
  tweets = api.search(q="あ",count=200)
  username = "all"
  get_tweets.tweet_save_text(tweets,username,output_file)
  get_tweets.tweet_save_data(tweets,username,output_file)

  
  for page in pages:
    #tweets = api.user_timeline(count=200, page=page)
    tweets = api.search(q="あ",count=200, page=page)

    username = "all"

    get_tweets.tweet_save_text(tweets,username,output_file)
    get_tweets.tweet_save_data(tweets,username,output_file)
  """

  tweets = api.search(q="あ",count=200)
  username = "10"
  get_tweets.tweet_save_text(tweets,username,output_file)
  get_tweets.tweet_save_data(tweets,username,output_file)  
  next_max_id = tweets[-1].id
  for i in range(2,1200):
    tweets = api.search(q="あ",count=200,max_id=next_max_id-1)
    next_max_id = tweets[-1].id
    username = "10"
    get_tweets.tweet_save_text(tweets,username,output_file)
    get_tweets.tweet_save_data(tweets,username,output_file)
    time.sleep(8)
    
  return tweets

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-o','--output_path', action = 'store')
  args = parser.parse_args()
  output_file = args.output_path


  tweet_data = get_tweet_page_all("10", 3000)

