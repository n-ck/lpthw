from nose.tools import *
from bin.app import app
from tests.tools import assert_response

def test_index():
	# check that we get a 303 on the / URL
	resp = app.request("/")
	# print "test 1 %s" % resp
	assert_response(resp, status="303")

	# test our first GET request to /game
	resp = app.request("/game")
	# print "test 2 %s" % resp
	assert_response(resp)

	# session dict:
	# {'ip': u'127.0.0.1', 'room': None, 'session_id': 'e5f756478a4a324b84deb8535015ea88b02d9629'}

	# make sure default values work for the form
	resp = app.request("/game", method="POST")
	# print "test 3 %s" % resp
	assert_response(resp, contains=None)

	## test that we get expected values
	data = "shoot!"
	resp = app.request("/game", method="POST", data=data)
	# print resp.data
	assert_response(resp, contains="You Died!")