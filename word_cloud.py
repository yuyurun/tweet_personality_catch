# coding:UTF-8

import MeCab as mc
import argparse

def load_data(filename):
  texts = []
  with open(filename,"r") as f:
    for row in f:
      print(row)
      texts.append(row)
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
  return output


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('-i','--input_path', action = 'store')
  args = parser.parse_args()
  input_file = args.input_path

  texts = load_data(input_file)
  output = mecab_word(texts)
  print(output)
