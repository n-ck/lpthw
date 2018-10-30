## Working scan function, passes all 6 tests
def scan(sentence):
	sentence = sentence.lower()
	splitsentence = sentence.split()

	directions = ["north", "south", "east", "west",
				  "down", "up", "left", "right", "back"]
	verbs = ["go", "stop", "kill", "eat"]
	stopwords = ["the", "in", "of", "from", "at", "it"]
	nouns = ["door", "bear", "princess", "cabinet"]
	adverbs = ["abruptly", "firmly", "quickly"]

	newtuple = []

	while splitsentence != []:
		for word in splitsentence:
			try:
				int(word)
				param = "number"
				newword = int(splitsentence.pop())
				
				## another way to convert the string in a number:
				# singlenewword = splitsentence.pop()
				# neword = singlenewword.digit()

			except ValueError:
				newword = splitsentence.pop()
				# newword = newword.lower()

		 		if word in directions:
		 			param = "direction"

				elif word in verbs:
					param = "verb"

				elif word in stopwords:
					param = "stop"

				elif word in nouns:
					param = "noun"

				elif word in adverbs:
					param = "adverb"

				else:
					param = "error"

			tuplecombo = (param, newword)
			newtuple.append(tuplecombo)

	newtuple.reverse()
	return newtuple


## Test output:

print scan("north")

print scan("north south east")

print scan("ASDFADFASDF")

print scan("bear IAS princess")

print scan("1234")

print scan("3 91234")
