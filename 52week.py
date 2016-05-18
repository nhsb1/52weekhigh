#!/usr/bin/env python
from bs4 import BeautifulSoup
import urllib2
import html5lib
#from argparse import ArgumentParser 
import re

#url = 'http://www.barchart.com/stocks/high.php?_dtp1=0'
#urlvolume = 'http://www.barchart.com/stocks/vleaders.php?_dtp1=0'
url = 'http://www.barchart.com/stocks/low.php?_dtp1=0'

def getSoup():
	global url, target
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page, 'html.parser')
	target = soup.find_all('tr') #gets all stock, e.g. line '110alpha', but not prices or change
	return target

def getTickers(mysoup):
	tickers = []
	for item in mysoup:
		tickerdirty = str(item)
		tickerdirty = re.findall(r'(quotes/stocks/\w+)', tickerdirty) #finds all of the stocks in the list.
		tickerdirty = str(tickerdirty)
		tickerdirty = tickerdirty.replace("]", "")
		tickerdirty = tickerdirty.replace("[", "")
		tickerdirty = tickerdirty.replace("'", "")
		before, sep, tickerclean = tickerdirty.rpartition("/") #http://stackoverflow.com/questions/7660847/python-split-string-after-a-character
		tickerclean = str(tickerclean)
		if tickerclean:
			tickers.append(tickerclean)
	return tickers

mysoup = getSoup()
mytickers = []
mytickers = getTickers(mysoup)

for item in mytickers:
	print item
