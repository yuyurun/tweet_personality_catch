#!/usr/bin/env python
#-*- coding:utf-8 -*-
import re
import argparse
import pandas as pd

def clean_tweet(text):
    # 正規表現でIDとURL,ハッシュタグ、RTを消す
    rtpattern = 'RT'
    replypattern = '@[\w]+'
    hashpattern = '#[\w]+'
    urlpattern = 'https?://[\w/:%#\$&\?\(\)~\.=\+\-]+'
    processedtweets = []
    
    for text in texts:
       tweet = text
       i = re.sub(replypattern, '', tweet)
       i = re.sub(rtpattern, '', i)
       i = re.sub(hashpattern, '', i)
       i = re.sub(urlpattern, '', i)
       i = re.sub('\n', '', i)
       if isinstance(i, str) and not i.split(): # 怪しい
           pass
       else:
           processedtweets.append(i)
           print(i)
    processedtweetsDataFrame = pd.Series(processedtweets)
    newDF = pd.DataFrame({'text': processedtweetsDataFrame})
    return newDF
    
def load_data(filename):
  texts = []
  with open(filename,"r") as f:
    for row in f:
      print(row)
      texts.append(row)
  return texts

def main():
    text = ''
    with open('./../dataset/tweets.csv', 'r') as f:
        text = f.read()
    newDF = clean_tweet(text)
    newDF.to_csv('./../dataset/processedtweets.csv')

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--input_path', action = 'store')
    args = parser.parse_args()
    input_file = args.input_path
    texts = load_data(input_file)
    newDF = clean_tweet(texts)
    newDF.to_csv(input_file + 'clean.csv')
