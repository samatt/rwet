#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-search
#search based on geolocation information
#
#-----------------------------------------------------------------------
from twitter import *
import sys
import re
import random
import urllib


# User inputs search string and geocode file
search = sys.argv[1]
locationFile = sys.argv[2]
tweets =  dict()
places = dict()

#read coordinates from text file into a dictionary2
#in this example file used is latlong.txt
for line in open(locationFile):
  line = line.strip()
  names = line.split(":")
  if len(names)>1:
  	places[names[0]] = names[1].split("$")


  
# create twitter API object
twitter = Twitter()

#oAuth object required for twitter verification
oauth = OAuth(
	#insert OAuth stuff here
	)
               
twitter = Twitter(domain='api.twitter.com',
                  auth=oauth,
                  api_version='1.1')




# open a file to write al the incoming tweets to. This file is also the input to tweetdict.py
output = file("tweets.txt","a")

# Choose a random place to use for the geo code.
# Current options are NY,LA,London,New Delhi, Bombay
code = places[random.choice(places.keys())][random.randint(0,3)]

#needed to concatenate the string like this otherwise I was getting erros in the search query
#something to do with %20 being substituted for end of string or whitespace.
code = code + ",10mi"
code.strip()

#used a loop sometimes to get a variety of results per script execution
#for pagenum in range(1, 11):

#Search Twitter!
query = twitter.search.tweets(q = search,geocode = code ,rrp=100)

#Do stuff with the result!
data = query.items()

#I figured out the structure by reverse engineering what was coming in from the API
#Im sure there is a  more effecient way of doing this. But this worked for me.

for tuples in data:	
	for lists in  tuples:
		if (type(lists)==dict):
			print 'No of tweets: %d' % lists[u'count'] 
		elif (type(lists)==list): 
			for dicts in lists:
				#Each tweet was contained in  a dict sttructure with a lot of metadata
				#This is how i parsed it to only store the data I cared about.
				if dicts['text']:
					user = dicts['user'] ['name']
					user = user.encode('ascii', 'replace')
					text =  dicts['text'] 
					text = text.encode('ascii', 'replace')
					print text
					#not all tweets had the geolocation info in their metadata
					if dicts[u'place']:
						print dicts['place']['name']
						place = dicts['place']['name']
						tweets[place] = text
						placeType = dicts['place']['place_type']
						
						#Used | as  a delimitter because , was coming up in  a lot of tweets.
						row = "%s|%s|%s|%s|%s \n"%(search,user,text,place,placeType)
						output.write(row)
					else:
						row = "%s|%s|%s \n"%(search,user,text)
						output.write(row)

#print "done page: %d" % (pagenum)			
output.close()


