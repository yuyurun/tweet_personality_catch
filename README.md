# tweet_personality_catch

Twitterの分析用のリポジトリ

## tweet取得(user)
python get_tweets.py -u ${name} -o ../data/tweet/personal/

## tweet取得(search)
検索ワードは決め打ち
python get_tweets_r.py -o ../data/tweet/personal/

## tweetデータ前処理
python cleaning.py -i ../data/tweet/personal/tweet_text_${name}.txt

## 単語、固有名詞、動詞、形容詞と副詞、bigram、trigramの頻度順出力
python word_count.py -i ../data/tweet/personal/tweet_text_${name}.clean.csv &> ../data/tweet/personal/bigram_${name}.txt

## マルコフ連鎖DB格納
python StoreTweetDB.py -i ../data/tweet/personal/tweet_text_${name}.clean.csv -u ${name}

## 文生成
python  GenerateText.py -f はじめの単語 

## 名詞だけ取得


## 特徴単語の取得
* ../data/tweet/personal/tfidfの下に名詞だけのファイルおく
`python tfidf.py`


