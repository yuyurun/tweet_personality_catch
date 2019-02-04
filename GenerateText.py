#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os.path
import sqlite3
import random
import argparse

from PrepareChain import PrepareChain


class GenerateText(object):
    """
    Generate text class
    """
    

    def __init__(self, username ,n=5):
        """
        initialized class
        @param n How_many_sentences_generated
        """
        self.n = n
        self.username = username
        self.DB_PATH = "/Users/hashizumeyuriko/dip/workspace/tweet_personality_catch/db/chain_" + args.username + ".db"
        self.DB_SCHEMA_PATH = "/Users/hashizumeyuriko/dip/workspace/tweet_personality_catch/sql/schema_"+ args.username +".sql"

    def generate(self):
        """
        generate method
        @return Generated_sentences
        """
        # There are no DB file raise error
        print('in generte')
        if not os.path.exists(self.DB_PATH):
            raise IOError("DB FILE was not found")
        # open DB
        print('open db')
        con = sqlite3.connect(self.DB_PATH)
        con.row_factory = sqlite3.Row
        print('con')
        generated_lines = []

        print('before range')
        for i in range(self.n):
            print(i)
            text = self._generate_sentence(con)
            print('text', len(text))
            print(args.first_word,end = "")
            print(text, flush=True)
            generated_lines.append(text)


        con.close()

        return generated_lines

    def _generate_sentence(self, con):
        """
        generate line randomly
        @param con DBobject
        @return generated_line
        """
        morphemes = []

        print('_generate_sentence')
        #first_triplet = self._get_first_triplet(con)
        first_triplet = self._get_first_triplet_in(con)
        morphemes.append(first_triplet[1])
        morphemes.append(first_triplet[2])
        print('morphemes')
        while morphemes[-1] != PrepareChain.END:
            prefix1 = morphemes[-2]
            prefix2 = morphemes[-1]
            triplet = self._get_triplet(con, prefix1, prefix2)
            morphemes.append(triplet[2])
        
        result = "".join(morphemes[:-1])

        return result

    def _get_chain_from_DB(self, con, prefixes):
        """
        get chain data from DB
        @param con DBobject
        @param prefixes rules_of_prefix_getting_chain tuple or list
        @return chain_list
        """
        username = self.username
        sql = "SELECT prefix1, prefix2, suffix, freq FROM chain_freqs_" + username + " WHERE prefix1 = ?"
        if len(prefixes) == 2:
            sql += " and prefix2 = ?"

        result = []

        # get from DB
        cursor = con.execute(sql, prefixes)
        for row in cursor:
            result.append(dict(row))
        return result

    def _get_first_triplet(self, con):
        """
        get first triplet randomly
        @param con DBobject
        @return first_triplet
        """
        prefixes = (PrepareChain.BEGIN,)

        print('_get_first_triplet')
        chains = self._get_chain_from_DB(con, prefixes)
        print('chains')
        triplet = self._get_probable_triplet(chains)
        print('triplet')
        return (triplet["prefix1"], triplet["prefix2"], triplet["suffix"])

    def _get_first_triplet_in(self, con):
        """
        get first triplet randomly
        @param con DBobject
        @return first_triplet
        はじめの単語を指定
        """
        #prefixes = (PrepareChain.BEGIN,)

        # 1単語目の指定
        prefixes = (args.first_word,)
        print('_get_first_triplet')
        chains = self._get_chain_from_DB(con, prefixes)
        print('chains')
        triplet = self._get_probable_triplet(chains)
        print('triplet')
        return (triplet["prefix1"], triplet["prefix2"], triplet["suffix"])
    
    def _get_triplet(self, con, prefix1, prefix2):
        """

        @param con DBobject
        @param prefix1 prefix1
        @param prefix2 prefix2
        @return triplet(tuple)
        """
        # BEGINをprefix1としてチェーンを取得
        prefixes = (prefix1, prefix2)

        # チェーン情報を取得
        chains = self._get_chain_from_DB(con, prefixes)

        # 取得したチェーンから、確率的に1つ選ぶ
        triplet = self._get_probable_triplet(chains)

        return (triplet["prefix1"], triplet["prefix2"], triplet["suffix"])

    def _get_probable_triplet(self, chains):
        """
        random choice
        @param chains list_of_chain
        @return random chosen_chain
        """
        # 確率配列
        probability = []
        # 確率に合うように、インデックスを入れる
        for (index, chain) in enumerate(chains):
            for j in range(chain["freq"]):
                probability.append(index)


        # ランダムに1つを選ぶ
        chain_index = random.choice(probability)

        return chains[chain_index]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f','--first_word', action = 'store')
    parser.add_argument('-u','--username', action = 'store')
    args = parser.parse_args()
    first_word = args.first_word
    username = args.username
    generator = GenerateText(username=username)
    print(generator.generate())

