## Working scan function, passes all 6 tests
def scan(sentence):
	splitsentence = sentence.split()

	directions = ["north", "south", "east", "west",
				  "down", "up", "left", "right", "back"]
	verbs = ["go", "stop", "kill", "eat"]
	stopwords = ["the", "in", "of", "from", "at", "it"]
	nouns = ["door", "bear", "princess", "cabinet"]

	newtuple = []

	while splitsentence != []:
		for word in splitsentence:
			try:
				int(word)
				param = "number"
				newword = int(splitsentence.pop())

			except ValueError:
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

## This was the function first, needed to be rewritten
def scan_working(sentence):
	splitsentence = sentence.split()

	directions = ["north", "south", "east", "west",
				  "down", "up", "left", "right", "back"]
	verbs = ["go", "stop", "kill", "eat"]
	stopwords = ["the", "in", "of", "from", "at", "it"]
	nouns = ["door", "bear", "princess", "cabinet"]

	newtuple = []

	## working code but numbers aren't working:

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
				try:
					int(word)
					param = "number"
					newword = int(word)

				except ValueError:
					param = "error"

			# elif int(word) == True:
			# 	newword = int(word)
			# 	param = "number"

			# else:
			# 	param = "error"

			tuplecombo = (param, newword)
			newtuple.append(tuplecombo)

	newtuple.reverse()
	return newtuple


## Test output:

# print scan("north")

# print scan("north south east")

# print scan("ASDFADFASDF")

# print scan("bear IAS princess")

# print scan("1234")

# print scan("3 91234")
