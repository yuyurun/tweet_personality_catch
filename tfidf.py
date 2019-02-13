import os
from sklearn.feature_extraction.text import TfidfVectorizer




class Tfidf(object):
  target_dir = "../data/tweet/personal/tfidf"


  def token_dict(self):
    dic = {}
    for subdir, dirs, files in os.walk(self.target_dir):
      for file in files:
        #print(file)
        file_path = os.path.join(subdir, file)
        f = open(file_path,'r')
        text = f.read()
        dic[file] = text
        f.close()
    return dic

  # TF-IDF ベクタライザーで読み込む関数
  # 文章をどう「ぶつ切りにする」かを定義しておく
  # とりま使ってないです
  def tokenize(self, text):
      words = text.rstrip().split("\n")
      return list(set(words))



  def analyze(self):
    dic = {}
   
    token_dic = self.token_dict()
    # 文書内に30回までの単語について
    #tfidf = TfidfVectorizer(tokenizer=self.tokenize, max_df=30)
    tfidf = TfidfVectorizer(max_df=4)
 
    #print(token_dic)
    # text渡す(配列)
    tfs = tfidf.fit_transform(token_dic.values())
    feature_names = tfidf.get_feature_names()
    #print(tfidf.vocabulary_)

    i = 0
    for k, v in token_dic.items():
      # 文書名、TF-IDFスコアのペアを辞書にする
      d = dict(zip(feature_names, tfs[i].toarray()[0]))
      #print(len(d))
      """  
      count = 0
      for l in d:
        if count < 3:
          print(l)
        count += 1
      """
      #print(d)

      #print(d[2])
      # TFIDFの高い順にソートする
      score = [(x, d[x]) for x in sorted(d, key=lambda x:-d[x])]
      word = [x for x in sorted(d, key=lambda x:-d[x])]
      # スコアの高いものから100こ
      #print(k)
      print(word[:10])
      #print(score[:10])
      dic[k] = score[:10]
      i += 1

    print(str(i))

    return dic



if __name__ == '__main__':
  tfidf = Tfidf()
  dic = tfidf.analyze()
  #print(dic)
