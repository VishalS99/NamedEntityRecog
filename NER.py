#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 10:47:55 2019

@author: vishal
"""
import requests
import sys
from bs4 import BeautifulSoup
import nltk
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')

import re
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import conlltags2tree, tree2conlltags
from pprint import pprint
def preprocess(sent):
    sent = nltk.word_tokenize(sent)
    sent = nltk.pos_tag(sent)
    return sent


def crawl(page,weburl):
    url = weburl
    code = requests.get(url)
    plain = code.text
    paraCorpusInitial = []
    headCorpusInitial = []
    paraCorpusFinal = []
    headCorpusFinal = []
    s = BeautifulSoup(plain, "html.parser")
    for divs in s.find_all('div',{'class': 'g'}):
        links= divs.find('a')['href']
        #print(divs);
        links = links[:links.find("&")]
        links = links[7:]
        print('Link: ' + links)
        if links[:5] == 'https':
            content = requests.get(links)
            s2 = BeautifulSoup(content.text,"html.parser")

            for h in s2.find_all(re.compile('^h[1-6]$')):
                data = h.getText()
                headCorpusInitial.append(data)
                # print(data);
            for p in s2.find_all("p"):
                data = p.getText()
                paraCorpusInitial.append(data)

        cp = nltk.RegexpParser('NP: {<DT>?<JJ>*<NN>}')

        for h in headCorpusInitial:
            sent = preprocess(h)
            # print(sent)
            headCorpusFinal.append(sent)
        
        for p in paraCorpusInitial:
            sent = preprocess(p)
            # print(sent)
            paraCorpusFinal.append(sent)

        i=0

        for h in headCorpusFinal:
            cs = cp.parse(h)
            # print(cs)
            headCorpusFinal[i] = cs
            i = i+1

        i=0

        for p in paraCorpusFinal:
            cs = cp.parse(p)
            # print(cs)
            paraCorpusFinal[i] = cs
            i = i+1


        for h in headCorpusFinal:
            iob_tagged = tree2conlltags(h)
            # pprint(iob_tagged)


        for p in paraCorpusFinal:
            iob_tagged = tree2conlltags(p)
            # pprint(iob_tagged)
        print("Possibilities in the titles :\n")
        for h in headCorpusInitial:
            ne_tree = nltk.ne_chunk(pos_tag(word_tokenize(h)))
            print (ne_tree)
            
        print("Possibilities in the Paragraphs :\n")

        for p in paraCorpusInitial:
            ne_tree = nltk.ne_chunk(pos_tag(word_tokenize(p)))
            print (ne_tree)
           


url = 'https://www.google.com/search?q='
print("########## Entity Recognition ##########")
print ("Enter the first name, last name , location, organisation ");
print("First Name: ")
fname = input()
print("Last Name: ")
lname = input()
print("Location: ")
loc = input()
print("Organisation: ")
org = input()
url = url + fname + '+' + lname + '+' + loc + '+' + org
crawl(100,url)