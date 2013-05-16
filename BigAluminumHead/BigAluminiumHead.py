from twitter import *
from wordnik import *
import sys
import re
import random
import urllib
import pprint
import markov
import OSC
import time, threading


def getRelatedWords(search):
	searchList = list()
	apiKeyWordnik = '#####'
	apiUrlWordnik= 'http://api.wordnik.com/v4'
	searchWord = search
	client = swagger.ApiClient(apiKeyWordnik,apiUrlWordnik)
	wordApi = WordApi.WordApi(client)
	wordList = wordApi.getRelatedWords(searchWord,relationshipTypes='same-context')

	for things in wordList:
		tempWords = things.words
		searchList = [w.encode('ascii','replace') for w in tempWords]
	return searchList

def removeTwitterCrap(w):
  w = re.sub(r'RT',' ',w)
  w = re.sub(r'@\w+\b',"", w)
  w = re.sub(r'http:.+\b',"", w)
  w = re.sub(r'#.+\b'," ", w)
  w = re.sub(r'&amp\b',"", w)
  w = re.sub(r'.+;\b'," ", w)
  w = re.sub(r'\b[lL][oO][lL]\b'," ", w)
  return w

def tweetStatus(new_status):
	#twitter stuff
	twitter = Twitter()
	consumer_key = "#####"
	consumer_secret = "######"
	access_key = "######"
	access_secret = "######"
	
	auth = OAuth(access_key, access_secret, consumer_key, consumer_secret)
	twitter = Twitter(auth = auth)

	results = twitter.statuses.update(status = new_status)
	print "updated status: %s" % new_status

def getTweets(query, mydict):
	#twitter stuff
	twitter = Twitter()

	oauth = OAuth(
		'######', 
		'######', 
		'######',
		'######'
		)

	twitter = Twitter(domain='api.twitter.com',
	                  auth=oauth,
	                  api_version='1.1')

	results = twitter.search.tweets(q = query,rrp=100)
	#Do stuff with the result!
	data1 = results.items()
	mydict[query] = list()
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
						text = removeTwitterCrap(text)
						mydict[query].append(text)

	return mydict


def lookForMoodStart(chain, word1):

	line_1 = list()

	for line in chain:

		mode = random.randint(1,3)

		if mode == 1:
			for matching_string in re.findall(r'\b \w+ %s .{2,30}$' % word1,line) :
				line_1.append(matching_string)
		if mode == 2:
			for matching_string in re.findall(r'\b \w+ \w+ %s .{2,30}$' % word1,line) :
				line_1.append(matching_string)
		if mode == 3:
			for matching_string in re.findall(r'\b \w+ \w+ \w+ %s .{2,30}$' % word1,line) :
				line_1.append(matching_string)
	return line_1	

def lookForMoodMiddle(chain, word1):

	line_2 = list()

	for line in chain:

		mode = random.randint(1,3)

		if mode == 1:
			for matching_string in re.findall(r'\b \w+ %s \w+ \w+ \w+ \w+ \w+' % word1,line) :
				line_2.append(matching_string)
		if mode == 2:
			for matching_string in re.findall(r'\b \w+ \w+ %s \w+ \w+ \w+ \w+' % word1,line) :
				line_2.append(matching_string)
		if mode == 3:
			for matching_string in re.findall(r'\b \w+ \w+ \w+ \w+ %s \w+ \w+' % word1,line) :
				line_2.append(matching_string)
	return line_2	

def lookForMoodEnd(chain, word1):

	line_3 = list()

	for line in chain:
		for matching_string in re.findall(r'\b \w+ %s .{2,30}$' % word1,line) :
			line_3.append(matching_string)
		
	return line_3	

def getMarkovChain(mydict,index):
	chains = list()
	#print index
	generator = CharacterMarkovGenerator(n=5, max=300)
	for line in mydict[index]:
		line = line.strip()
		#print line
		generator.feed(line)
	
	for i in range(300):
		chains.append(generator.generate())
	return chains	

		
	chains.append(generator.generate())
class CharacterMarkovGenerator(markov.MarkovGenerator):
	def tokenize(self, text):
		return list(text)
	def concatenate(self, source):
		return ''.join(source)
class myOSC(object):

	def __init__(self):
		self.send_address = '127.0.0.1', 9000
		self.receive_address = '127.0.0.1', 7000
		self.c = OSC.OSCClient()
		self.c.connect( self.send_address ) # set the address for all following messages
		self.s = OSC.OSCServer(self.receive_address)
		self.s.addDefaultHandlers()
		#self.s.addMsgHandler("/word", self.receiveWordHandler) # adding our function 
		# just checking which handlers we have added
		print "Registered Callback-functions are :"
		
		# for addr in self.s.getOSCAddressSpace():
		# 	print addr


		# Start OSCServer
		print "\nStarting OSCServer. Use ctrl-C to quit."
		self.st = threading.Thread( target = self.s.serve_forever )
		self.st.start()

	def sendOSC(self, w):
		msg = OSC.OSCMessage()
		msg.setAddress("/word") # set OSC address
		msg.append( w) # string
		self.c.send(msg)
		
def printing_handler (addr, tags, stuff, source):
	print "---"
	print "received new osc msg from %s" % OSC.getUrlStr(source)
	print "with addr : %s" % addr
	print "typetags %s" % tags
	print "data %s" % stuff
	global test 
	test = stuff
	print len(test)
	print "---"	
#wordnik stuff
if __name__ == '__main__':

	test = "a"
 	mine = myOSC()
 	mine.s.addMsgHandler("/word",printing_handler) # adding our function 
 	mine.sendOSC("sending")	
	

	try :
	    while 1 :
	        time.sleep(5)
	       	print test
	        if(test[0]=='tweet'):

				tweetDict = dict()	
				words =getRelatedWords(test[1])
				test = 'a'				
				number1 = random.randint(0,len(words) - 1 )
				number2 = random.randint(0,len(words) - 1 )
				number3 = random.randint(0,len(words) - 1 )


				while number1 == number2 or number2 == number3 or number1 == number3:
					number2 = random.randint(0,len(words) - 1 )
					number3 = random.randint(0,len(words) - 1 )


				print words[number1]
				print words[number2]
				print words[number3]

				tweetDict = getTweets(words[number1],tweetDict)
				tweetDict = getTweets(words[number2],tweetDict)
				tweetDict = getTweets(words[number3],tweetDict)
				# words = tweetDict.keys()
				#pprint.pprint(tweetDict)
				# print words[number1]

				list1 = list()
				list2 = list()
				list3 = list()

				count1 = 0
				count2 = 0
				count3 = 0

				while len(list1) <= 0 and count1 < 10:
					count1 = count1 + 1
					chain1 = getMarkovChain(tweetDict,words[number1])
					list1 = lookForMoodStart(chain1,words[number1])
				
				print count1

				while len(list2) <= 0 and count2 < 10:
					count2 = count2 + 1
					chain2 = getMarkovChain(tweetDict,words[number2])
					list2 = lookForMoodMiddle(chain2,words[number2])
				
				print count2

				while len(list3) <= 0 and count3 < 10:
					count3 = count3 + 1
					chain3 = getMarkovChain(tweetDict,words[number3])
					list3 = lookForMoodEnd(chain3,words[number3])

				print count3
				tweet = " "
				if count1 < 10:
					tweet = random.choice(list1) + '\n'
				else:
					tweet = "   \n"	
					
				if count2 < 10:
					tweet += random.choice(list2) + '\n'
				else:
					tweet = "   \n"	
				
				if count3 < 10:
					tweet += random.choice(list3) + '\n'
				else:
					tweet = "   \n"	
				
				if count3 >= 10 and count2 >= 10 and count1 >= 10:
					tweet += 'Im not in the mood'
				mine.sendOSC(tweet)
				print tweet	
				tweetStatus(tweet)

	except KeyboardInterrupt :
		    print "\nClosing OSCServer."
		    mine.s.close()
		    print "Waiting for Server-thread to finish"
		    mine.st.join() ##!!!
		    print "Done"




