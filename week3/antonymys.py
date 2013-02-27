import sys
import random

antonyms = dict()
source_file = sys.argv[1] # first argument passed on command line

for line in open(source_file):
  line = line.strip()
  #split into sentences 
  sentences = line.split("\n")
  for sentence in sentences:
    # for each sentence split the word from its antonyms
    words = sentence.split("-")
    #strip any remaining white spaces
    words = [word.strip() for word in words]
    line = line.strip()
    #if there is more than one antonym put it in a list otherwise keep it as a 
    #single string
    antys = [word.split(',') if ',' in word else word for word in words ]
    #add the word as the key and antonyms in a dictionary
    antonyms[antys[0]] = antys[1]


#print antonyms

# read each line from standard input; split line into words; for each word,
# get a random word beginning with the same letter from source_alpha
for line in sys.stdin:
  line = line.strip()
  words = line.split(" ")
  output = list()
  for word in words:
      if word in antonyms:
        source_words = antonyms[word]
        if(type(antonyms[word]) == list):
          #if there is a list of antonyms select one randomly
          output.append(random.choice(source_words))
        else:    
          output.append(source_words)
      else:
        output.append(word)
  print " ".join(output)

