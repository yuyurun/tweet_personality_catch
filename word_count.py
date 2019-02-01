# coding:UTF-8


import MeCab as mc
import argparse
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd
import nltk

import word_cloud


def word_count(text):
  nltk.download('punkt')
  tokens = nltk.word_tokenize(text) 

  freqdist = nltk.FreqDist(tokens)
  print(freqdist.most_common(500))

def word_count_bi(text):
  nltk.download('punkt')
  tokens = nltk.word_tokenize(text) 

  #Create your bigrams 
  bgs = nltk.bigrams(tokens) 
  
  #compute frequency distribution for all the bigrams in the text 
  fdist = nltk.FreqDist(bgs) 
  print(fdist.most_common(500))

def mecab_word_meisi(texts):
  output = []
  for text in texts:
    tagger = mc.Tagger('-Ochasen -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd/')
    tagger.parse('')
    #enc_text = text.encode('utf-8')
    result = tagger.parseToNode(text)
    while(result):
      if result.surface != "":  # ヘッダとフッタを除外
        word_type = result.feature.split(",")[0]
        if word_type in ["名詞"]:
          output.append(result.surface)
      result = result.next
      if result is None:
        break

  text = ' '.join(output)
  return text

def mecab_word_dousi(texts):
  output = []
  for text in texts:
    tagger = mc.Tagger('-Ochasen -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd/')
    tagger.parse('')
    #enc_text = text.encode('utf-8')
    result = tagger.parseToNode(text)
    while(result):
      if result.surface != "":  # ヘッダとフッタを除外
        word_type = result.feature.split(",")[0]
        if word_type in ["動詞"]:
          output.append(result.surface)
      result = result.next
      if result is None:
        break

  text = ' '.join(output)
  return text

def mecab_word_keihuku(texts):
  output = []
  for text in texts:
    tagger = mc.Tagger('-Ochasen -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd/')
    tagger.parse('')
    #enc_text = text.encode('utf-8')
    result = tagger.parseToNode(text)
    while(result):
      if result.surface != "":  # ヘッダとフッタを除外
        word_type = result.feature.split(",")[0]
        if word_type in ["形容詞", "副詞"]:
          output.append(result.surface)
      result = result.next
      if result is None:
        break

  text = ' '.join(output)
  return text

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('-i','--input_path', action = 'store')
  args = parser.parse_args()
  input_file = args.input_path

  texts = word_cloud.load_csv(input_file)
  output = word_cloud.mecab_word(texts)
  word_count(output)
  output = mecab_word_meisi(texts)
  word_count(output)
  output = mecab_word_dousi(texts)
  word_count(output)
  output = mecab_word_keihuku(texts)
  word_count(output)
