# -*- coding:utf8 -*-
import urllib2
from slack import *
from bs4 import BeautifulSoup

url= urllib2.urlopen('https://www.packtpub.com/packt/offers/free-learning')
soup = BeautifulSoup(url, 'html.parser',from_encoding="utf-8")
f1 = soup.find_all('div','dotd-title')
f2 = str(f1[0].h2.string).strip()
print f2

if __name__ == '__main__':
    post_slack(f2)

