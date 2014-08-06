#!/usr/bin/env python
import sys, os, urllib2, time
from bs4 import BeautifulSoup

def notify(title, subtitle, message, open):
	t = '-title {!r}'.format(title)
	s = '-subtitle {!r}'.format(subtitle)
	m = '-message {!r}'.format(message)
	o = '-open {!r}'.format(open)
	os.system('/usr/local/bin/terminal-notifier {}'.format(' '.join([m, t, s, o])))

def main():
	
	##### THIS IS THE LINE YOU REPLACE. EVERYTHING BETWEEN THE DOUBLE QUOTES ("")
	mainSearch = "http://www.craigslist.com/url-to-search"
	#####
	
	firstResponse = urllib2.urlopen(mainSearch)
	html1 = firstResponse.read()
	mainSoup = BeautifulSoup(html1)
	now = time.localtime()
	for link in mainSoup.findAll("a",{"class":"i"}):
		try:
			href = "http://sfbay.craigslist.org" + link.get("href")
			linkResponse = urllib2.urlopen(href)
			aptHTML = linkResponse.read()
			aptSoup = BeautifulSoup(aptHTML)
			postTime = time.strptime(aptSoup.time.get("datetime"), "%Y-%m-%dT%H:%M:%S-0700")
			minutesAgo = (time.mktime(now) - time.mktime(postTime)) / 60
			if minutesAgo < 30000:
				notify(
					title="Found an apartment!",
					subtitle=href,
					message=aptSoup.findAll("h2",{"class":"postingtitle"})[0].get_text().strip(),
					open=href
				)
		except Exception as e:
			pass

if __name__ == "__main__":
	main()
