import sys
import random
import re
#-----------------------------------------------------------------------
# twitter-poetry
# tweet verse generation
#
#-----------------------------------------------------------------------
tweets = dict()
keys = list()
lines = list()
users = list()

#output file of the geotweets script is taken as an input in this script
#This made it easier to seperate the functionality and helped while debugging
source_file = sys.argv[1] 


#A function full of regular expressions to get rid of common twitter terminology
#eg: @user, #tags, http://t.co.... Experimented with replacing them with random 'poetic' sounding words
def removeTwitterCrap(w):
  w = re.sub(r'RT','Stay free!',w)
  w = re.sub(r'@\w+\b',"", w)
  w = re.sub(r'http:.+\b',"", w)
  w = re.sub(r'#.+\b'," ", w)
  w = re.sub(r'&amp\b',"", w)
  w = re.sub(r'.+;\b'," ", w)
  w = re.sub(r'\b[lL][oO][lL]\b',"elation", w)
  return w


#Make a dictionary with all the tweets. The keys are the search queries.
for line in open(source_file):
  line = line.strip()
  sentences = line.split("|")
  
  # only parse if the data structure looks like it contains everything
  if len(sentences)>2:
    if sentences[0] in keys :
      tweets[sentences[0]].append([sentences[1],sentences[2]]) 
      
    else:  
      keys.append(sentences[0])
      tweets[sentences[0]] = []
      tweets[sentences[0]].append([sentences[1],sentences[2]])
  
#Randomly choose keys and spit out verses.
#On testing using a for loop with a lange number range prevents frequent repitition 
for pagenum in range(1, 50):
  key = random.choice(keys)
  size = len(tweets[key]) -1
  size =random.randint(0,size)

  #select a random tweet from a random search query
  test =tweets[key][size][1]
  
  #also keep the username inforamtion
  #experimented with using usernames fas verses too
  users.append(tweets[key][size][0])
  
  #self explanatory
  tweet =  removeTwitterCrap(test)
  tweet = tweet.strip()

  lines.append(tweet)
  
  
  #Regex Experiments
  # for matching_string in re.findall(r'\b\w+ [Yy]ou \w+', tweet):
  #   print lines.append(matching_string)

  # for matching_string2 in re.findall(r'\b\w+ \w+ I \w+', tweet):
  #   print lines.append(matching_string2)
    
  # for matching_string3 in re.findall(r'\b\w+ we \w+', tweet):
  #   print lines.append(matching_string3)



print random.choice(lines)
print random.choice(users)
print random.choice(lines)
print '\n'
print random.choice(users)
print random.choice(lines)
print random.choice(users)
print '\n'
print random.choice(lines)
print random.choice(users)
print random.choice(lines)
print '\n'
