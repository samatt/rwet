#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-search
#search based on geolocation information
#
#-----------------------------------------------------------------------
import json
from twitter import *

# create twitter API object
twitter = Twitter()
tweets =  dict()
oauth = OAuth(
	'935447275-f7CdYLCF13kby9H1cUwlYK4ZUR9Jeo4IoyMpvZ6h', 
	'giSYuMZb1cPH4YFUJVvBRVjmzyahKyWc7INyBDlXeQ', 
	'Rix6YbOOX4TnJbFiRrmkQw',
	'etdqOFKHKhafZVQDqJSt4xJ4ki8QsG5YHsc4BD4Eecw'
	)
               
twitter = Twitter(domain='api.twitter.com',
                  auth=oauth,
                  api_version='1.1',
                  format='json')
#             
#twitter = Twitter(domain='api.twitter.com',
#                  auth=oauth,
#                  api_version='1')

# perform a basic search 
# twitter API docs: https://dev.twitter.com/docs/api/1/get/search
query = twitter.search.tweets(q = "new cross",geocode = "51.474144,-0.035401,1km")

data = query.items()
#data = json.loads(query.items())
#print tweets

for tuples in data:	
	for lists in  tuples:
		#print item
		if (type(lists)==list):
			
			for dicts in lists:
				#print dicts.keys()
				if dicts['coordinates']:
				#print dic['user'] 
					print dicts['place'] 
				#print dic[u'coordinates'] 
			


