

def scan(sentence):
	splitsentence = sentence.split()

	directions = ["north", "south", "east", "west",
				  "down", "up", "left", "right", "back"]

	verbs = ["go", "stop", "kill", "eat"]

	stopwords = ["the", "in", "of", "from", "at", "it"]

	nouns = ["door", "bear", "princess", "cabinet"]

	numbers = range(0,10)

	newtuple = []

 	for word in splitsentence:
 		if word in directions:
 			param = "direction"

		elif word in verbs:
			param = "verb"

		elif word in stopwords:
			param = "stop"

		elif word in nouns:
			param = "noun"
			

	while splitsentence != []:
		for word in splitsentence:
			newword = splitsentence.pop()
			tuplecombo = (param, newword)
			newtuple.append(tuplecombo)

	return newtuple
 	
# # needs an if statement, if single word don't create a list, just print the tuple
# print scan("north")

# print scan("north south east")

# # this is working
# scan('south north east')


## Working for loop but only returns one tuple:

 	# for word in splitsentence:
 	# 	if word in directions:
 	# 		param = "direction"
 	# 		directiontuple = (param, word)
 	# 	 	newtuple.append(directiontuple)
 	# 	 	return newtuple

		# elif word in verbs:
		# 	param = "verb"
		# 	directiontuple = (param, word)
		# 	newtuple.append(directiontuple)
		# 	return newtuple

		# elif word in stopwords:
		# 	param = "stop"
		# 	directiontuple = (param, word)
		# 	return newtuple.append(directiontuple)

		# elif word in nouns:
		# 	param = "noun"
		# 	directiontuple = (param, word)
		# 	return newtuple.append(directiontuple)