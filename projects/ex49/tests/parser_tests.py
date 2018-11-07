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

def test_parse_verb():
	wordlist = [("verb", "kill"),("stop", "the"),("noun", "princess")]
	assert_equal(parser.parse_verb(wordlist), ("verb", "kill"))

	wordlist2 = [("noun", "princess"),("stop", "the"),("verb", "kill")]
	assert_raises(parser.ParserError,parser.parse_verb, wordlist2)

def test_parse_object():
	wordlist = [("noun", "princess")]
	assert_equal(parser.parse_object(wordlist), ("noun", "princess"))

	wordlist2 = [("verb", "kill")]
	assert_raises(parser.ParserError,parser.parse_object, wordlist2)


def test_parse_subject():
	wordlist = [("verb", "kill"),("noun", "princess")]
	subj = ("noun", "player")
	result = parser.parse_subject(wordlist, subj)
	assert_equal((result.subject, result.verb, result.object), ("player","kill","princess"))

	# wordlist2 = [("pronoun", "they"), ("adverb", "loudly")]
	# subj = ("adjunct","tomorrow")
	# result = parser.parse_subject(wordlist2, subj)
	# assert_raises(parser.ParserError,parser.parse_subject, result.subject, result.verb, result.object)


def test_parse_sentence():
	wordlist = [("verb", "kill"), ("noun", "princess")]
	result = parser.parse_sentence(wordlist)
	assert_equal((result.subject, result.object, result.verb), ("player","princess","kill"))

	# wordlist2 = [("adjunct", "yesterday"), ("noun", "princess")]
	# result = parser.parse_sentence(wordlist)
	# assert_raises(parser.ParserError,parser.parse_sentence, wordlist2)
