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
from ex45choices import Choices
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

		print "\n" + reasons[randomnumber]

		print "\nGame Over!\n"
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

		# get choices/answers and assign the list to a variable correctanswers
		correctanswers = Choices().entry_correct()
		incorrectanswers = Choices().entry_incorrect()

		flag = True
		user_input = raw_input("> ")

		# working while loop to check for correct and incorrect answers:
		while flag:
			if user_input in correctanswers:
				print "\nNext level:\n"
				flag = False

				# next step is to automatically send the user to the next level:
				print Generator('entry').nextlevel()
				exit(0)

				# youescaped = Escape()
				# youescaped()

			elif user_input in incorrectanswers:
				flag = False
				gameover = Caught()
				gameover()
			else:
				print "Try again:\n"
				user_input = raw_input("> ")

class Escape():
	# Class for the final scene of the game, when the user has
	# successfully escaped.
	def __init__(self):
		print "\nCongratulations, you successfully escaped with the money!\n"
		exit(0)


class Generator():
	def __init__(self, level):
		self.level = level

	def nextlevel(self):
		# initialize the Bank class 
		gameareas = Bank()

		# store the dictionary with bank areas in the variable 'levels'
		levels = gameareas.bank_areas()

		# loop through the dictionary get the current level and the next level:
		for key, value in levels.items():

			# check if the value in the dictionary is equal 
			# to the Generator class parameter:
			if value == self.level:
				currentlvl = key
				# get the last character of the dictionary key string and
				# save it as a new variable
				currentlvl = currentlvl.strip()[-1]
				# add 1 to the current level
				nextlvl = int(currentlvl) + 1
				# create the string of the next level
				getnext = "level %d" % nextlvl

				# return the nextlevel dictionary key
				return getnext

	## work in progress
	# def generatenext(self):

	# 	if self.level == "entry":
	# 		entrylevel = Entry()
	# 		entrylevel()
	# 	elif nextlevel() == 'level 1':



	## The generator class determines what level it is,
	## and what level is generated next:

	# 1. Get current level from the Class init
	# 2. Get all items from the dictionary
	# 3. Lookup where current level is in the dictionary
	# 4. Then return the number + 1 
	# 5. If the 

class StartGame():
	# start the game

	def load_areas(self):

		# initialize the Bank class 
		the_bank = Bank().bank_areas()
		# set the current level, this statement will return the dict value 'entry'
		currentlevel = the_bank['level 0']

		# initialize the GameScript class
		gamescript = GameScript()
		# load the level description that matches the current level
		print gamescript.level_description(currentlevel)

		# initialize the Level logic class
		levellogic = Level()
		# load the level logic class
		levellogic


class Vault():
	# last level of the game, guess the combination of the 
	# vault to enter and steal all the money in there.
	def crack_the_code(self):

		print "You arrived at the bank's vault, try to unlock the vault spin the wheel left or right"
	
		Vault().unlock_safe('right')		
		
	def unlock_safe(self, correct):

		self.correct = correct

		firstattempt = raw_input("> ")
		flag = True

		while flag:
			if firstattempt in correct:
				print "correct"
				flag = False
			else:
				print "try again"
				firstattempt = raw_input("> ")

# initialize the StartGame class and start the game:
StartGame().load_areas()

# Vault().crack_the_code()
