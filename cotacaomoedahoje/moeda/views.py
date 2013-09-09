# Create your views here.
from urllib2 import urlopen

_file = urlopen('http://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml')

import sys
from bs4 import BeautifulSoup as Soup

def parseLog(file):
	handler = file.read()
	soup = Soup(handler)
	for message in soup.findAll('cube'):
		msg_attrs = dict(message.attrs)
		if msg_attrs.has_key('currency'):
			print msg_attrs

parseLog(_file)