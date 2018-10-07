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



from ex45script import *


class Bank():
	#Has all rooms, doors, vault and tunnel
	def bank_areas(self):
		areas = {'level 0': 'entry', 'level 1': 'teller', 
				'level 2': 'back office', 'level 3': 'vault', 'level 4': 'tunnel'
			}

		# return statement so you can access the dictionary
		return areas


class Caught():
	# when you get caught by security/the police
	def __init__(self):
		print "You got caught!"
		exit(0)


class Level():
	# parent class for every level

	def __init__(self):
		user_input = raw_input("> ")

		if user_input != "":
			print "Next level"
		else:
			gameover = Caught()
			gameover()


class StartGame():
	# start the game

	def load_areas(self):

		the_bank = Bank().bank_areas()
		currentlevel = the_bank['level 0']

		gamescript = GameScript()
		gamescript.level_description(currentlevel)

		levellogic = Level()
		levellogic


class Vault():
	#
	pass

startgame = StartGame()
startgame.load_areas()
