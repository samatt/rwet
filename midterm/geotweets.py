#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-search
#search based on geolocation information
#
#-----------------------------------------------------------------------
import json
from twitter import *
import sys
import csv
import time

# create twitter API object
twitter = Twitter()
tweets =  dict()
search = 'journey'
oauth = OAuth(
	'935447275-f7CdYLCF13kby9H1cUwlYK4ZUR9Jeo4IoyMpvZ6h', 
	'giSYuMZb1cPH4YFUJVvBRVjmzyahKyWc7INyBDlXeQ', 
	'Rix6YbOOX4TnJbFiRrmkQw',
	'etdqOFKHKhafZVQDqJSt4xJ4ki8QsG5YHsc4BD4Eecw'
	)
               
twitter = Twitter(domain='api.twitter.com',
                  auth=oauth,
                  api_version='1.1')


# perform a basic search 
# twitter API docs: https://dev.twitter.com/docs/api/1/get/search
 #until Returns tweets generated before the given date. Date should be formatted as YYYY-MM-DD.

# open a file to append, and create a CSV writer object
#csvfile = file("test.csv", "a")
output = file("tweets.txt","a")
#csvwriter = csv.writer(csvfile)
#row = [ "user", "text", "place", "type"]

#for pagenum in range(1, 11):
query = twitter.search.tweets(q = search,geocode = "40.770496,-73.989089,10mi",rrp=100)
#query = twitter.search.tweets(q = "the",rpp=100,lang='en')
data = query.items()
#data = json.loads(query.items())
#print tweets

for tuples in data:	
	for lists in  tuples:
		print type(lists)

		if (type(lists)==dict):
			print 'No of tweets: %d' % lists[u'count'] 
			#print lists

		elif (type(lists)==list): 
			
			for dicts in lists:
				#print dicts['geo']
				if dicts['text']:
					#print dicts['user'] 
					user = dicts['user'] ['name']
					user = user.encode('ascii', 'replace')
					text =  dicts['text'] 
					text = text.encode('ascii', 'replace')
					#print text
					if dicts[u'place']:
						print dicts['place']['name']
						place = dicts['place']['name']
						tweets[place] = text
						placeType = dicts['place']['place_type']
						#row = [ user, text, place, placeType ]
						row = "%s|%s|%s|%s|%s \n"%(search,user,text,place,placeType)
						#user+"|"+text+"|"+place+"|"+placeType 
						output.write(row)
						#csvwriter.writerow(row)
					else:
						#row = [ user, text]
						#row = +user+"|"+text
						row = "%s|%s|%s \n"%(search,user,text)
						output.write(row)
						#csvwriter.writerow(row)
					

					#print dicts[u'text'] 
#print "done page: %d" % (pagenum)			
output.close()
#csvfile.close()

