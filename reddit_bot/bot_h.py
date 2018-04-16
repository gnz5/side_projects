from bot_keywords import *
# strips a string of several non-alphabetical characters such
# as '!' and '?' and sets all characters to lowercase
def process(input):
	input = input.lower()
	input = input.replace('!', ' ')
	input = input.replace('?', ' ')
	input = input.replace('.', ' ')
	input = input.replace(',', ' ')
	input = input.replace('(', ' ')
	input = input.replace(')', ' ')
	input = input.replace('@', ' ')
	input = input.replace('#', ' ')
	input = input.replace('$', ' ')
	input = input.replace('/', ' ')
	input = input.replace('\\', ' ')
	input = input.replace(';', ' ')	
	words = input.split(' ')
	return words

# takes in a string containing a single word and outputs the
# definition if the word is a valid keyword, otherwise returns None
def test(input):	
	words = process(input)
	for str in words:
		if(str in keywords.keys()):
			print(str)
			return keywords[str]
	return None
