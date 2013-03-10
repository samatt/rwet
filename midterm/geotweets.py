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
import re
import random
import urllib




def removeTwitterCrap(w):
  w = re.sub(r'RT',' ',w)
  w = re.sub(r'@\w+\b'," ", w)
  w = re.sub(r'http:.+\b'," ", w)
  return w

search = sys.argv[1]
locationFile = sys.argv[2]
tweets =  dict()
places = dict()

for line in open(locationFile):
  line = line.strip()
  #split into sentences 
  names = line.split(":")
  if len(names)>1:
  	#print names[0]
  	places[names[0]] = names[1].split("$")
#print places


  
# create twitter API object
twitter = Twitter()


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
output = file("tweets.txt","a")

code = places[random.choice(places.keys())][random.randint(0,3)]
#code = places['NY'][random.randint(0,3)]
code = code + ",10mi"
#print urllib.unquote(code)
code.strip()
#for pagenum in range(1, 11):
print code
query = twitter.search.tweets(q = search,geocode = code ,rrp=100)
#query = twitter.search.tweets(q = search,geocode = "40.770496,-73.989089,10mi",rrp=100)

data = query.items()
print data
#data = json.loads(query.items())
#print code

for tuples in data:	
	for lists in  tuples:
		#print type(lists)

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
					#text = removeTwitterCrap(text);
					print text
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

