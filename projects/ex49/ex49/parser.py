class ParserError(Exception):
	pass


class Sentence():

	def __init__(self, subject, verb, object):
		# remember we take ('noun', 'princess') tuples and convert them
		self.subject = subject[1]
		self.verb = verb[1]
		self.object = object[1]


def peek(word_list):
	## A way to 'peek' at a potential tuple so we can make some decisions.
	if word_list:
		word = word_list[0]
		return word[0]
	else:
		return None

def match(word_list, expecting):
	## A way to 'match' different types of tuples that we 
	## expect in our subject-verb-object setup.
	if word_list:
		word = word_list.pop(0)

		if word[0] == expecting:
			return word
		else:
			return None

	else:
		return None

def skip(word_list, word_type):
	## A way to 'skip' things we do not care about, 
	## like stop words.
	while peek(word_list) == word_type:
		match(word_list, word_type)

def parse_verb(word_list):
	skip(word_list, 'stop')

	if peek(word_list) == 'verb':
		return match(word_list, 'verb')
	else:
		raise ParserError("Expected a verb next.")

def parse_object(word_list):
	skip(word_list, 'stop')
	next = peek(word_list)

	if next == 'noun':
		return match(word_list, 'noun')
	if next == 'direction':
		return match(word_list, 'direction')
	else:
		raise ParserError("Expected a noun or direction next.")

def parse_subject(word_list, subj):
	verb = parse_verb(word_list)
	obj = parse_object(word_list)

	return Sentence(subj, verb, obj)

def parse_sentence(word_list):
	skip(word_list, 'stop')

	start = peek(word_list)

	if start == 'noun':
		subj = match(word_list, 'noun')
		return parse_subject(word_list, subj)
	elif start == 'verb':
		# assume the subject is the player then
		return parse_subject(word_list, ('noun', 'player'))
	else:
		raise ParserError("Must start with subject, object or ver or not: %s" % start)


### Test wordlist:

# wordlist = [("verb", "kill"),("stop", "the"),("noun", "player")]


### 3 Main functions:

# print "\npeek function:"
# print peek(wordlist)
## Output: verb

# print "\nmatch function:"
# print match(wordlist, "verb")
## Output: ('verb', 'kill')

# print "\nskip function:"
# print skip(wordlist, "stop")
## Output: None


### 4 Parse functions:

# print "\nparse_verb function:"
# print parse_verb(wordlist)
## Output: ('verb', 'kill')

# wordlist2 = [("noun", "princess")]
# print "\nparse_object function:"
# print parse_object(wordlist2)
## Output: ('noun', 'princess')

# wordlist3 = [("verb", "kill"),("noun", "player")]
# subj = ("subject", "cat")
# print "\nparse_subject function:"
# result = parse_subject(wordlist3, subj)
# print "subject = %s, object = %s, verb = %s" % (result.subject, result.object, result.verb) 

# wordlist4 = [("verb", "kill"), ("noun", "princess")]
# print "\nparse_sentence function:"
# result = parse_sentence(wordlist4)

# print "subject = %s, object = %s, verb = %s" % (result.subject, result.object, result.verb) 
