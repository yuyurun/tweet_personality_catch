#!/usr/bin/env python
#-*- coding:utf-8 -*-
import re
import argparse
import pandas as pd
import word_cloud

#import xml.etree.ElementTree as ET

def get_person(texts):
  person = False
  data = []
  for text in texts:
    if '== 登場人物 ==' in text:
      person = True
    elif person == True:
      if not "===" in text:
        if "== " in text:
          person = False
        elif ": " in text:
          data.append(text)
          print(text)
  return data

def out_file(data):
  f = open(args.input_path + ".get","w")
  for d in data:
    d = re.sub(r'\|.*\]\]',"",d)
    d = re.sub(r'&.*;',"",d)
    d = d.replace("[[","")
    d = d.replace("]]","")
    d = d.replace("&lt;ref&gt","。")
    d = d.replace("。","。\n")
    d = d.replace(": ","")
    d = d.replace("\n\n","\n")
    if not "声 " in d:
      if "。\n" in d:
        f.write(d)





if __name__=='__main__':
    """
    tree = ET.parse('../data/DBpedia/jawiki-20160407-pages-articles.xml')
    root = tree.getroot()
    print(root.tag)
    print(root.attrib)
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--input_path', action = 'store')
    args = parser.parse_args()
    input_file = args.input_path
    texts = word_cloud.load_data(input_file)
    data = get_person(texts)
    out_file(data)
    
