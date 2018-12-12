# coding : UTF-8

import settings
import tweepy
import argparse

def get_tweet(acountname, num):
  consumer_key    = settings.CK
  consumer_secret = settings.CS
  access_key      = settings.AK
  access_secret   = settings.AS

  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_key, access_secret)
  api = tweepy.API(auth)

  tweets = api.user_timeline(acountname, count=num)

  return tweets

def tweet_save_text(tweets,acountname,filepath):
  username = acountname.replace("@","")
  with open(filepath + "/tweet_text_"  + username + ".txt","w") as f:
    for tweet in tweets:
      f.write(tweet.text)
      f.write("\n")

def tweet_save_data(tweets,acountname,filepath):
  username = acountname.replace("@","")
  with open(filepath + "/tweet_data_"  + username + ".txt","w") as f:
    for tweet in tweets:
      f.write(tweet.text)
      f.write("\n")
      f.write(str(tweet.favorite_count))
      f.write("\n")
      f.write(str(tweet.retweet_count))
      f.write("\n")
      f.write(str(tweet.created_at))
      f.write("\n")

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-u', '--user_name', action = 'store')
  parser.add_argument('-o','--output_path', action = 'store')
  args = parser.parse_args()
  username = args.user_name
  output_file = args.output_path


  tweet_data = get_tweet(username, 10000)
  tweet_save_text(tweet_data,username,output_file)
  tweet_save_data(tweet_data,username,output_file)

  #for tweet in tweet_data:
  #  print(tweet.text, "/n")

