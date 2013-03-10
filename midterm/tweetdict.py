import sys
import random
import re

tweets = dict()
keys = list()
lines = list()
line_2 = list()
line_3 = list()
source_file = sys.argv[1] # first argument passed on command line
def removeTwitterCrap(w):
  w = re.sub(r'RT',' ',w)
  w = re.sub(r'@\w+\b'," ", w)
  w = re.sub(r'http:.+\b'," ", w)
  w = re.sub(r'#.+\b'," ", w)
  w = re.sub(r'&amp\b'," ", w)
  return w

for line in open(source_file):
  line = line.strip()
  
  #split into sentences 
  sentences = line.split("|")
  # for sentence in sentences:
  if len(sentences)>2:
    #print sentences
    if sentences[0] in keys :
      tweets[sentences[0]].append([sentences[1],sentences[2]]) 
      
    else:  
      keys.append(sentences[0])
      tweets[sentences[0]] = []
      tweets[sentences[0]].append([sentences[1],sentences[2]])


  #tweets[sentences[1]] = sentences[0],sentences[2]
  
#print tweets

for pagenum in range(1, 11):
#  print tweets[keys[0]][5]
  key = random.choice(keys)
  print key
  size = len(tweets[key]) -1
  size =random.randint(0,size)
  #print tweets
  test =tweets[key][size][1]
  
  tweet =  removeTwitterCrap(test)
  tweet = tweet.strip()

  lines.append(tweet)
  # for matching_string in re.findall(r'\b\w+ [Yy]ou \w+', tweet):
  #   print line_1.append(matching_string)

  # for matching_string2 in re.findall(r'\b\w+ \w+ I \w+', tweet):
  #   print line_2.append(matching_string2)
    
  # for matching_string3 in re.findall(r'\b\w+ we \w+', tweet):
  #   print line_3.append(matching_string3)



print random.choice(lines)
print random.choice(lines)
print random.choice(lines)

