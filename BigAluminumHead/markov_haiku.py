import markov
import random
import re
chains = list();

from sys import argv


def lookForMood1(chain, word1):

	line_1 = list()

	for line in chain:

		mode = random.randint(1,3)

		if mode == 1:
			for matching_string in re.findall(r'\b\w+ %s \w+ \w+ \w+ \w+ \w+' % word1,line) :
				line_1.append(matching_string)

		if mode == 2:
			for matching_string in re.findall(r'\b\w+ \w+ %s \w+ \w+ \w+ \w+' % word1,line) :
				line_1.append(matching_string)

		if mode == 3:
			for matching_string in re.findall(r'\b\w+ \w+ \w+ \w+ %s \w+ \w+' % word1,line) :
				line_1.append(matching_string)

	return line_1		


def lookForMood2(chain, word2):

	line_2 = list()

	for line in chain:

		mode = random.randint(1,3)

		if mode == 1:
			for matching_string in re.findall(r'\b\w+ %s \w+ \w+ \w+ \w+ \w+' % word2,line) :
				line_2.append(matching_string)

		if mode == 2:
			for matching_string in re.findall(r'\b\w+ \w+ %s \w+ \w+ \w+ \w+' % word2,line) :
				line_2.append(matching_string)

		if mode == 3:
			for matching_string in re.findall(r'\b\w+ \w+ \w+ \w+ %s \w+ \w+' % word2,line) :
				line_2.append(matching_string)

	return line_2		


def lookForMood3(chain, word3):

	line_3 = list()

	for line in chain:

		mode = random.randint(1,3)

		if mode == 1:
			for matching_string in re.findall(r'\b\w+ %s \w+ \w+ \w+ \w+ \w+' % word3,line) :
			line_3.append(matching_string)

		elif mode == 2:for matching_string in re.findall(r'\b\w+ \w+ %s \w+ \w+ \w+' % word3,line) :
			line_3.append(matching_string)print "I'm in mode 2"

		elif mode == 3:
			for matching_string in re.findall(r'\b\w+ \w+ \w+ \w+ %s \w+' % word3,line) :
			line_3.append(matching_string)
	
	return line_3		


  

class CharacterMarkovGenerator(markov.MarkovGenerator):
	def tokenize(self, text):
		return list(text)
	def concatenate(self, source):
		return ''.join(source)

if __name__ == '__main__':

	import sys

	word1 = sys.argv[1]
	word2 = sys.argv[2]
	word3 = sys.argv[3]

	generator = CharacterMarkovGenerator(n=5, max=300)
	# lines = set()
	for line in sys.stdin:
		line = line.strip()
		generator.feed(line)

	for i in range(300):
		#print generator.generate()
		chains.append(generator.generate())


#print lookForMood(chains,word1)
list1 = lookForMood1(chains,word1)
list2 = lookForMood2(chains,word2)
list3 = lookForMood3(chains,word3)


print random.choice(list1)
print random.choice(list2)
print random.choice(list3)

# print random.choice(lookForMood(chains))
# print random.choice(lookForMood(chains))

