

def scan(sentence):
	splitsentence = sentence.split()

	directions = ["north", "south", "east", "west",
				  "down", "up", "left", "right", "back"]

	newdirections = []

 	for word in splitsentence:
 		if word in directions:
 			param = "direction"
 			directiontuple = (param, word)
 			newdirections.append(directiontuple)

 	print newdirections
 	
# needs an if statement, if single word don't create a list, just print the tuple
scan('north')

# this is working
scan('south north east')

