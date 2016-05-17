#!/usr/bin/env python
from bs4 import BeautifulSoup
import urllib2
import html5lib
import time
from argparse import ArgumentParser 
import re

url = 'http://www.barchart.com/stocks/high.php?_dtp1=0'

def getSoup():
	global url, target
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page, 'html.parser')
	target = soup.find_all('tr') #gets all stock, e.g. line '110alpha', but not prices or change



		# fullname = clean1.split(",")[0]
		# lastname = fullname.split(",")[0].split()[-1]
		#firstname = re.findall(r'([a-zA-Z]\w+)', fullname)[0]
		#<a href="/quotes/stocks/AEM">AEM</a></td>

tickers = []
ticker2=[]
ticker3=[]
count = 0 
mysoup = getSoup()
for item in target:
	stuff = str(item)
	#stuff = stuff.split("/quotes/stocks/")
	#print stuff
	stuff2 = re.findall(r'(quotes/stocks/\w+)', stuff) #finds all of the stocks in the list; needs cleanup.
	test = str(stuff2)
	before, sep, after = test.rpartition("/") #http://stackoverflow.com/questions/7660847/python-split-string-after-a-character
	#good = test.rsplit('/')[1]
	after = str(after)
	after = after.replace("]", "")
	after = after.replace("'", "")
	#after = after.strip()
	if len(after) >= 2: #if there's stuff in the list 'stuff2' append it to tickers
		tickers.append(after)
		ticker2.append(sep)
		ticker3.append(before)

#print tickers
for item in tickers:
	print item


	

#print tickers
	#print cleanerstuff
	#print str(count) + "alpha", item

	#count = count+1

# count2 = 0
# for item in target2:
# 	print str(count2) + "beta", item
# 	count2 = count+1
#print target

#print mysoup

