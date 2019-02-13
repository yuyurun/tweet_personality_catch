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




if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('-i','--input_path', action = 'store')
  args = parser.parse_args()
  input_file = args.input_path

  texts = word_cloud.load_csv(input_file)
  output = word_cloud.mecab_word(texts)
  #word_count(output)
  output = word_count.mecab_word_meisi(texts)
  out_text(output)
