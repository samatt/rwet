
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
	 

for line in sys.stdin:
	line = line.strip()
	#make a list of words from the line in stdin
	words = [w for w in line.split(" ")]
	# translate each word in that line
	translated = [translator(w) for w in words]
	print " ".join(translated)






