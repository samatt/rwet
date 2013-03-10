import sys
import random

tweets = dict()
keys = list()
source_file = sys.argv[1] # first argument passed on command line

for line in open(source_file):
  line = line.strip()
  
  #split into sentences 
  sentences = line.split("|")
  # for sentence in sentences:
  if len(sentences)>2:
    print sentences
    if sentences[0] in keys :
      tweets[sentences[0]].append([sentences[1],sentences[2]]) 
      
    else:  
      keys.append(sentences[0])
      tweets[sentences[0]] = []
      tweets[sentences[0]].append([sentences[1],sentences[2]])


  #tweets[sentences[1]] = sentences[0],sentences[2]
  
print tweets

#for pagenum in range(1, 11):
#  print tweets[keys[0]][5]




