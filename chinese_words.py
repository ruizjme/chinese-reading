#!/usr/bin/python

import urllib.request as urllib2
from bs4 import BeautifulSoup
import re


def getDict():
    print("Getting wiktionary list...")
    web = "https://en.wiktionary.org/wiki/Appendix:Mandarin_Frequency_lists/1-1000"
    page = urllib2.urlopen(web)
    soup = BeautifulSoup(page,'html.parser')
    all_items = soup.find_all('li')

    p = re.compile(r'^[\w]+, ([\w]+) \(([\w]+)\) - (.+)$')

    pinyinDict = {}

    print("Parsing wiktionary list...")
    for item in all_items:
        i = item.get_text()
        m = p.match(i)

        if m is not None:
            wordMandarin = m.group(1)
            wordPinyin = m.group(2)
            wordMeaning = m.group(3)

            pinyinDict[wordPinyin] = wordMeaning

            # print('{:<6}{:<8}{:<15}'.format(wordMandarin,wordPinyin,wordMeaning))

    return pinyinDict
