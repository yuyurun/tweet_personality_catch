# coding:UTF-8


import MeCab as mc
import argparse
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd

def load_data(filename):
  texts = []
  with open(filename,"r") as f:
    for row in f:
      print(row)
      texts.append(row)
  return texts

def load_csv(csv_path):
  texts = []
  df = pd.read_csv(csv_path)
  texts = df['text']
  return texts

def mecab_word(texts):
  output = []
  for text in texts:
    tagger = mc.Tagger('-Ochasen -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd/')
    tagger.parse('')
    #enc_text = text.encode('utf-8')
    result = tagger.parseToNode(text)
    while(result):
      if result.surface != "":  # ヘッダとフッタを除外
        word_type = result.feature.split(",")[0]
        if word_type in ["形容詞", "動詞","名詞", "副詞"]:
          output.append(result.surface)
      result = result.next
      if result is None:
        break

  text = ' '.join(output)
  return text

def word_cloud(text):
  stop_words = ['https', 'co']
  fpath = "/Library/Fonts/KodomoRounded.otf"
  wordcloud = WordCloud(background_color="white",font_path=fpath, width=900, height=500,stopwords=set(stop_words)).generate(text)

  plt.figure(figsize=(15,12))
  plt.imshow(wordcloud)
  plt.axis("off")
  plt.show()


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('-i','--input_path', action = 'store')
  args = parser.parse_args()
  input_file = args.input_path

  #texts = load_data(input_file)
  texts = load_csv(input_file)
  output = mecab_word(texts)
  print(output)
  word_cloud(output)
