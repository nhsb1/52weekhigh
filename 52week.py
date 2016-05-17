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

count = 0 
mysoup = getSoup()
for item in target:
	stuff = str(item)
	stuff2 = re.findall(r'(quotes/stocks/\w+)', stuff)
	if stuff2 is not "":
		print stuff2
	
	

print stuff2
	#print cleanerstuff
	#print str(count) + "alpha", item

	#count = count+1

# count2 = 0
# for item in target2:
# 	print str(count2) + "beta", item
# 	count2 = count+1
#print target

#print mysoup

