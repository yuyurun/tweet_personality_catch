#!/usr/bin/env python
#-*- coding:utf-8 -*-

from PrepareChain import PrepareChain
import pandas as pd
from tqdm import tqdm
import argparse

def storeTweetDB(csv_path):
    """
    read tweetcsv
    """
    df = pd.read_csv(csv_path)

    tweets = df['text']
    print(len(tweets))
    
    chain = PrepareChain(tweets[0],args.username)
    chain.path(args.username)
    triplet_freqs = chain.make_triplet_freqs()
    chain.save(triplet_freqs, True)

    for i in tqdm(tweets[1:]):
        print(i)
        chain = PrepareChain(i,args.username)
        triplet_freqs = chain.make_triplet_freqs()
        chain.save(triplet_freqs, False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--input_path', action = 'store')
    parser.add_argument('-u','--username', action = 'store')
    args = parser.parse_args()
    input_file = args.input_path
    storeTweetDB(input_file)

