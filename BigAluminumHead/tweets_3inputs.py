#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-search1
#search1 based on geolocation information
#
#-----------------------------------------------------------------------
from twitter import *
import sys
import re
import random
import urllib
import pprint

def removeTwitterCrap(w):
  w = re.sub(r'RT',' ',w)
  w = re.sub(r'@\w+\b',"", w)
  w = re.sub(r'http:.+\b',"", w)
  w = re.sub(r'#.+\b'," ", w)
  w = re.sub(r'&amp\b',"", w)
  w = re.sub(r'.+;\b'," ", w)
  w = re.sub(r'\b[lL][oO][lL]\b'," ", w)
  return w

# User inputs search1 string and geocode file
search1 = sys.argv[1]
search2 = sys.argv[2]
search3 = sys.argv[3]
tweets =  dict()
places = dict()

# #read coordinates from text file into a dictionary2
# #in this example file used is latlong.txt
# for line in open(locationFile):
#   line = line.strip()
#   names = line.split(":")
#   if len(names)>1:
#   	places[names[0]] = names[1].split("$")


  
# create twitter API object
twitter = Twitter()

#oAuth object required for twitter verification
oauth = OAuth(
	'#####', 
	'#####', 
	'#####',
	'#####'
	)
               
twitter = Twitter(domain='api.twitter.com',
                  auth=oauth,
                  api_version='1.1')




# open a file to write al the incoming tweets to. This file is also the input to tweetdict.py
output = file("tweets1.txt","a")




#----------------- FIRST Argument -------------------#

query1 = twitter.search.tweets(q = search1,rrp=100)
#Do stuff with the result!
data1 = query1.items()

#I figured out the structure by reverse engineering what was coming in from the API
#Im sure there is a  more effecient way of doing this. But this worked for me.

for tuples in data1:	
	
	for elements in  tuples:
		if (type(elements)==dict):
			print 'No of tweets: %d' % elements[u'count'] 

		elif (type(elements)==list): 

			for dicts in elements:
				#pprint.pprint(dicts)
				#Each tweet was contained in  a dict sttructure with a lot of metadata1
				#This is how i parsed it to only store the data1 I cared about.
				if dicts['text']:
					user = dicts['user'] ['name']
					user = user.encode('ascii', 'replace')
					text =  dicts['text'] 
					text = text.encode('ascii', 'replace')

					print removeTwitterCrap(text)
					#not all tweets had the geolocation info in their metadata
					if dicts[u'place']:
						print dicts['place']['name']
						place = dicts['place']['name']
						tweets[place] = text
						placeType = dicts['place']['place_type']
						
						#Used | as  a delimitter because , was coming up in  a lot of tweets.
						row = "%s \n"%(removeTwitterCrap(text))
						output.write(row)
					else:
						row = "%s \n"%(removeTwitterCrap(text))
						output.write(row)


#----------------- SECOND Argument -------------------#

query2 = twitter.search.tweets(q = search2,rrp=100)
#Do stuff with the result!
data2 = query2.items()

#I figured out the structure by reverse engineering what was coming in from the API
#Im sure there is a  more effecient way of doing this. But this worked for me.

for tuples in data2:	
	
	for elements in  tuples:
		if (type(elements)==dict):
			print 'No of tweets: %d' % elements[u'count'] 

		elif (type(elements)==list): 

			for dicts in elements:
				#pprint.pprint(dicts)
				#Each tweet was contained in  a dict sttructure with a lot of metadata2
				#This is how i parsed it to only store the data2 I cared about.
				if dicts['text']:
					user = dicts['user'] ['name']
					user = user.encode('ascii', 'replace')
					text =  dicts['text'] 
					text = text.encode('ascii', 'replace')

					print removeTwitterCrap(text)
					#not all tweets had the geolocation info in their metadata
					if dicts[u'place']:
						print dicts['place']['name']
						place = dicts['place']['name']
						tweets[place] = text
						placeType = dicts['place']['place_type']
						
						#Used | as  a delimitter because , was coming up in  a lot of tweets.
						row = "%s \n"%(removeTwitterCrap(text))
						output.write(row)
					else:
						row = "%s \n"%(removeTwitterCrap(text))
						output.write(row)

#----------------- THIRD Argument -------------------#

query3 = twitter.search.tweets(q = search3,rrp=100)
#Do stuff with the result!
data3 = query3.items()

#I figured out the structure by reverse engineering what was coming in from the API
#Im sure there is a  more effecient way of doing this. But this worked for me.

for tuples in data3:	
	
	for elements in  tuples:
		if (type(elements)==dict):
			print 'No of tweets: %d' % elements[u'count'] 

		elif (type(elements)==list): 

			for dicts in elements:
				#pprint.pprint(dicts)
				#Each tweet was contained in  a dict sttructure with a lot of metadata3
				#This is how i parsed it to only store the data3 I cared about.
				if dicts['text']:
					user = dicts['user'] ['name']
					user = user.encode('ascii', 'replace')
					text =  dicts['text'] 
					text = text.encode('ascii', 'replace')

					print removeTwitterCrap(text)
					#not all tweets had the geolocation info in their metadata
					if dicts[u'place']:
						print dicts['place']['name']
						place = dicts['place']['name']
						tweets[place] = text
						placeType = dicts['place']['place_type']
						
						#Used | as  a delimitter because , was coming up in  a lot of tweets.
						row = "%s \n"%(removeTwitterCrap(text))
						output.write(row)
					else:
						row = "%s \n"%(removeTwitterCrap(text))
						output.write(row)


#print "done page: %d" % (pagenum)			
output.close()


