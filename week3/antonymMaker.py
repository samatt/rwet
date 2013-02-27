import sys
import random


file1 = sys.argv[1] # first argument passed on command line
file2 = sys.argv[2]
list1 = list()
list2 = list()
list3 = list()

for line in open(file1):
	line = line.strip()
	list1.append(line)

for line in open(file2):
	line = line.strip()
	list2.append(line)

zipped = zip(list1,list2)
print type(zipped)
for word in zipped:
 	sent = word[0]+' - '+word[1]
 	list3.append(sent)

print '\n'.join(list3)	

  	