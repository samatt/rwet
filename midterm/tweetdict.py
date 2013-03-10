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
  
#print tweets

for pagenum in range(1, 11):
#  print tweets[keys[0]][5]
  test =tweets[random.choice(len(keys)][1]
  print test
  # for line in txt1:
  #   line = line.strip()

  #   for matching_string in re.findall(r'\b\w+ [Yy]ou \w+', line):
  #     line_1.append(matching_string)

  #   for matching_string2 in re.findall(r'\b\w+ \w+ I \w+', line):
  #   line_2.append(matching_string2)
    
  #   for matching_string3 in re.findall(r'\b\w+ we \w+', line):
  #   line_3.append(matching_string3)



  # print random.choice(line_1)
  # print random.choice(line_2)
  # print random.choice(line_3)

