
#my first python program
import sys

searchString = 'a'
trString = 'e'

def translator(w):	
	
	if w.__contains__(searchString):
		tr = w.replace(searchString,trString)
		return tr	
	else:
		return w
	 

print "Please enter the char you wish to change"
searchString = raw_input()
print "Source Char:" + searchString
print "Please enter the char you wish to add"
trString = raw_input()
print "Dest Char:" + searchString
for line in sys.stdin:
	line = line.strip()
	#make a list of words from the line in stdin
	words = [w for w in line.split(" ")]
	# translat each word in that line
	translated = [translator(w) for w in words]
	print " ".join(translated)






