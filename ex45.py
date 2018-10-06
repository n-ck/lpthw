## Ex45 Game

# import multiple files
# use one class per room
# make one class that knows about the rooms and runs them
# spend a week creating this game
# use classes, functions, dicts, lists and loops
# purpose of the lesson is to teach how to structure classes
# that need other classes inside other files

## Game description:
# Open a vault to steal money from a bank
# Escape through a tunnel
# Get into the bank
# Pass the laser security
# Don't get seen by a camera




# from blabla import blabla
from ex45script import *


class Bank():
	#Has all rooms, doors, vault and tunnel
	def bank_areas(self):
		areas = ['entry', 'teller', 'back office', 'vault', 'tunnel']

		print areas[0]

class Caught():
	# when you get caught by security/the police
	pass

class StartGame():
	#
	pass

class Vault():
	#
	pass


startgame = Bank()
startgame.bank_areas()

level = GameScript()
level.game_level('teller')