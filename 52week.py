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


tickers = []

count = 0 
mysoup = getSoup()
for item in target:
	tickerdirty = str(item)
	tickerdirty = re.findall(r'(quotes/stocks/\w+)', tickerdirty) #finds all of the stocks in the list.
	tickerdirty = str(tickerdirty)
	before, sep, tickerclean = tickerdirty.rpartition("/") #http://stackoverflow.com/questions/7660847/python-split-string-after-a-character
	tickerclean = str(tickerclean)
	tickerclean = tickerclean.replace("]", "")
	tickerclean = tickerclean.replace("[", "")
	tickerclean = tickerclean.replace("'", "")
	#if len(tickerclean) >= 1: #if there's stuff in the list 'stuff2' append it to tickers
	#	tickers.append(tickerclean)
	if tickerclean:
		tickers.append(tickerclean)

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

