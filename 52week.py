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
	return target

def getTickers(mysoup):
	#tickerdirty = []
	tickers = []
	#print mysoup
	for item in mysoup:
		tickers=[]
		tickerdirty = str(item)
		#print tickerdirty
		tickerdirty = re.findall(r'(quotes/stocks/\w+)', tickerdirty) #finds all of the stocks in the list.
		tickerdirty = str(tickerdirty)
		#print tickerdirty
		before, sep, tickerclean = tickerdirty.rpartition("/") #http://stackoverflow.com/questions/7660847/python-split-string-after-a-character
		tickerclean
		tickerclean = str(tickerclean)
		tickerclean = tickerclean.replace("]", "")
		tickerclean = tickerclean.replace("[", "")
		tickerclean = tickerclean.replace("'", "")
		
		if tickerclean:
			print tickerclean
			tickers.append(tickerclean)
		#print tickers
	#if len(tickerclean) >= 1: #if there's stuff in the list 'stuff2' append it to tickers
	#	tickers.append(tickerclean)
	#if tickerclean:
	#	print tickers
	return tickers




count = 0 
mysoup = getSoup()
mytickers = []

myticker = []
mytickers = getTickers(mysoup)
for item in mytickers:
	print item


#print tickers
# for item in mytickers:
# 	print item

