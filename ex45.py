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
import random


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

		reasons = ['You got noticed on the security camera', 
		'The alarm went off','The police caught you',
		'You set off a motion-detection laser',
		'A bank security guard caught you'
		]

		randomnumber = random.randint(0,4)

		print reasons[randomnumber]
		# you need this exit statement or python will throw an error
		exit(0)


class Level():
	# parent class for every level
	def __init__(self):
		entrylevel = Entry()
		entrylevel()

class Entry():
	# the opening level/scene of the game (entry of the bank)
	def __init__(self):
		user_input = raw_input("> ")

		if user_input != "":
			print "\nNext level"
			youescaped = Escape()
			youescaped()
		else:
			gameover = Caught()
			gameover()

class Escape():
	# Class for the final scene of the game, when the user has
	# successfully escaped.
	def __init__(self):
		print "\nCongratulations, you successfully escaped with the money!\n"
		exit(0)

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
	# last level of the game, guess the combination of the 
	# vault to enter and steal all the money in there.
	pass

startgame = StartGame()
startgame.load_areas()
