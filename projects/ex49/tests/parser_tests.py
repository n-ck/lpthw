from nose.tools import *
from ex49 import parser

def test_peek():
	wordlist = wordlist = [("verb", "kill"),("stop", "the"),("noun", "princess")]
	assert_equal(parser.peek(wordlist), "verb")
	assert_equal(parser.peek(""), None)

def test_match():
	wordlist = wordlist = [("verb", "kill"),("stop", "the"),("noun", "princess")]
	assert_equal(parser.match(wordlist, "verb"), ("verb", "kill"))
	assert_equal(parser.match(wordlist, "stop"), ("stop", "the"))
	assert_equal(parser.match(wordlist, "run"), None)

def test_skip():
	wordlist = [("verb", "kill"),("stop", "the"),("noun", "princess")]
	assert_equal(parser.skip(wordlist, "kill"), None)

def test_parse_objects():
	pass


# def test_directions():
# 	assert_equal(lexicon.scan("north"), [('direction', 'north')])
# 	result = lexicon.scan("north south east")
# 	assert_equal(result, [('direction', 'north'),
# 						  ('direction', 'south'),
# 						  ('direction', 'east')])

# def test_verbs():
# 	assert_equal(lexicon.scan("go"), [('verb', 'go')])
# 	result = lexicon.scan("go kill eat")
# 	assert_equal(result, [('verb', 'go'),
# 						  ('verb', 'kill'),
# 						  ('verb', 'eat')])

# def test_stops():
# 	assert_equal(lexicon.scan("the"), [('stop', 'the')])
# 	result = lexicon.scan("the in of")
# 	assert_equal(result, [('stop', 'the'),
# 						  ('stop', 'in'),
# 						  ('stop', 'of')])

# def test_nouns():
# 	assert_equal(lexicon.scan("bear"), [('noun', 'bear')])
# 	result = lexicon.scan("bear princess")
# 	assert_equal(result, [('noun', 'bear'),
# 						  ('noun', 'princess')])

# def test_adverbs():
# 	assert_equal(lexicon.scan("abruptly"), [('adverb', 'abruptly')])
# 	result = lexicon.scan("quickly firmly")
# 	assert_equal(result, [('adverb', 'quickly'),
# 						   ('adverb', 'firmly')])

# def test_numbers():
# 	assert_equal(lexicon.scan("1234"), [('number', 1234)])
# 	result = lexicon.scan("3 91234")
# 	assert_equal(result, [('number', 3),
# 						  ('number', 91234)])

# def test_errors():
# 	assert_equal(lexicon.scan("ASDFADFASDF"), [('error', 'ASDFADFASDF')])
# 	result = lexicon.scan("bear IAS princess")
# 	assert_equal(result, [('noun', 'bear'),
# 						  ('error', 'IAS'),
# 						  ('noun', 'princess')])