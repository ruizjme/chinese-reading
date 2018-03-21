#!/usr/bin/python

import urllib.request as urllib2
from bs4 import BeautifulSoup
import re

import chinese_words

def getStory(web):
    print("Getting pinyin story...")
    page = urllib2.urlopen(web)
    soup = BeautifulSoup(page,'html.parser')
    return soup.find_all('p')

pinyinDict = chinese_words.getDict()
inList = 0
notInList = 0
paragraphs = getStory('http://www.pinyin.info/readings/pinyin_riji_duanwen/01_dashui_guohou.html')
# paragraphs = getStory('http://www.pinyin.info/readings/pinyin_riji_duanwen/02_laoye_zaoqi_d_gongzuo.html')

print("Generating output html...")
with open('story-output.html', 'w') as output:

    for item in paragraphs:
        item = item.get_text()
        item = item.split()

        output.write('<p>')
        for word in item:
            if word.strip('.').strip(',').lower() in pinyinDict.keys():
                output.write('<a href="https://en.pons.com/translate/chinese-english/{}" data-toggle="tooltip" data-placement="top" title="{}" target="blank">{}</a>\n '.format(word.strip('.').strip(',').lower(), pinyinDict[word.strip('.').strip(',').lower()], word))
                inList += 1
            else:
                output.write('<a style="color:#750707" href="https://en.pons.com/translate/chinese-english/{}" target="blank">{}</a>\n '.format(word.strip('.').strip(','), word))
                notInList += 1
        output.write('</p>')

print((inList/(inList+notInList))*100, "% of words in this story are in the most used ", len(pinyinDict.keys())," Chinese words.")
