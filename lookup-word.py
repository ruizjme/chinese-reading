#!/usr/bin/python

import urllib.request as urllib2
from bs4 import BeautifulSoup

web = "https://en.pons.com/translate/chinese-english/f%C4%93ich%C3%A1ng"
page = urllib2.urlopen(web)
soup = BeautifulSoup(page, 'html.parser')

print(soup.prettify())


# WIP
