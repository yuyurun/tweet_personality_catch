# coding:UTF-8


import MeCab as mc
import argparse
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd
import nltk

import word_cloud
import word_count

def out_text(output):  
  with open(args.input_path + ".meisi","w") as f:
      f.write(output)


# train data作るために1文ずつ
def mecab_word_meisi(texts):
  output = []
  f = open(args.input_path + ".meisi","w")
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
    for word in output:
      f.write(word + " ")
    f.write("\n")
    output = []


def mecab_word_meisi_csv(texts):
  output = []
  f = open(args.input_path + ".1080.csv","w")
  f.write("word , doc \n")
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
    if not "," in text:
      if len(text) < 80 and len(text) > 10:
        for word in output:
          f.write(word + " ")
        f.write("," + text)
        #f.write("\n")
    output = []

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('-i','--input_path', action = 'store')
  args = parser.parse_args()
  input_file = args.input_path

  texts = word_cloud.load_data(input_file)
  #output = word_cloud.mecab_word(texts)
  #word_count(output)
  #mecab_word_meisi(texts)
  mecab_word_meisi_csv(texts)
  #out_text(output)
