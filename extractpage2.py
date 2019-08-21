from BeautifulSoup import BeautifulSoup
import urllib2 
import re 
import sys

html_page = urllib2.urlopen(sys.argv[1])
soup = BeautifulSoup(html_page)
for link in soup.findAll('a'):
 print link.get('href')
