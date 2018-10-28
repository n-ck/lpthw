
def scan(sentence):
	splitsentence = sentence.split()

	directions = ["north", "south", "east", "west",
				  "down", "up", "left", "right", "back"]
	verbs = ["go", "stop", "kill", "eat"]
	stopwords = ["the", "in", "of", "from", "at", "it"]
	nouns = ["door", "bear", "princess", "cabinet"]

	newtuple = []

	for word in splitsentence:

		try:
			int(word)
			scannumber(sentence)
		except ValueError:
			scanword(sentence)

	## working code but numbers aren't working:
	
	# while splitsentence != []:
	# 	for word in splitsentence:
	# 		newword = splitsentence.pop()

	#  		if word in directions:
	#  			param = "direction"

	# 		elif word in verbs:
	# 			param = "verb"

	# 		elif word in stopwords:
	# 			param = "stop"

	# 		elif word in nouns:
	# 			param = "noun"

	# 		elif int(word):
	# 			newword = int(word)
	# 			param = "number"

	# 		else:
	# 			param = "error"

	# 		tuplecombo = (param, newword)
	# 		newtuple.append(tuplecombo)

	# newtuple.reverse()
	# return newtuple

def scanword(sentence):

	directions = ["north", "south", "east", "west",
				  "down", "up", "left", "right", "back"]
	verbs = ["go", "stop", "kill", "eat"]
	stopwords = ["the", "in", "of", "from", "at", "it"]
	nouns = ["door", "bear", "princess", "cabinet"]

	newtuple = []

	while splitsentence != []:
		for word in splitsentence:
			newword = splitsentence.pop()

	 		if word in directions:
	 			param = "direction"

			elif word in verbs:
				param = "verb"

			elif word in stopwords:
				param = "stop"

			elif word in nouns:
				param = "noun"

			else:
				param = "error"

			tuplecombo = (param, newword)
			newtuple.append(tuplecombo)

	newtuple.reverse()
	return newtuple


def scannumber(sentence):

	newtuple = []

	while splitsentence != []:
		for word in splitsentence:
			newword = splitsentence.pop()
	 		param = "number"
			tuplecombo = (param, newword)
			newtuple.append(tuplecombo)

	newtuple.reverse()
	return newtuple[]
 	
# # needs an if statement, if single word don't create a list, just print the tuple
# print scan("north")

# print scan("north south east")

print scan("1234")

print scan("3 91234")

# print scan("ASDFADFASDF")

# print scan("bear IAS princess")