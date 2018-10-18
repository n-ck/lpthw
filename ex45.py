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


from ex45script import GameScript
from ex45choices import Choices
import random


class Bank(object):
	# Has all rooms, doors, vault and tunnel
	
	def bank_areas(self):
		'''Store a list of all levels in the a variable'''
		areas = {'level 0': 'entry', 'level 1': 'teller', 
				'level 2': 'back office', 'level 3': 'vault', 
				'level 4': 'tunnel'
				}

		# return areas variable so you can access the dictionary
		return areas


class Caught(object):
	# when you get caught by security/the police

	def __init__(self):

		reasons = [
			'You got noticed on the security camera', 
			'The alarm went off',
			'The police caught you',
			'You set off a motion-detection laser',
			'A bank security guard caught you'
		]

		randomnumber = random.randint(0,4)

		print "\n" + reasons[randomnumber]

		print "\nGame Over!\n"
		# you need this exit statement or python will throw an error
		exit(0)


class Level(object):
	# parent class for every level

	# def __init__(self):
	# 	'''get the level name from the class parameter'''
	# 	entrylevel = Entry()
	# 	entrylevel.start()

	# def __init__(self):

		# self.correctanswers = Choices().entry_correct()
		# self.incorrectanswers = Choices().entry_incorrect()


	def answerloop(self, level):

		correctanswers = Choices().entry_correct()
		incorrectanswers = Choices().entry_incorrect()

		self.level = level
		flag = True
		user_input = raw_input("> ")
		attempts = 1

		# working while loop to check for correct and incorrect answers:
		while flag:
			if user_input in correctanswers:
				nextlevel = Teller().start()
				nextlevel
				flag = False
			elif user_input in incorrectanswers:
				flag = False
				gameover = Caught()
				gameover()
			elif attempts > 3:
				gameover = Caught()
				gameover()				
			else:
				print "Try again:\n"
				user_input = raw_input("> ")
				attempts = attempts + 1


	def nextlevel(self, level):

		if level == 'entry':
			Teller().start()
		else:
			Caught()


class Entry(Level):
	
	def __init__(self):
		# initialize the GameScript class
		gamescript = GameScript()
		# load the level description that matches the current level
		gamescript.level_description('entry')

	# the opening level/scene of the game (entry of the bank)
	# def __init__(self):

		# get choices/answers and assign the list to a variable correctanswers
		# correctanswers = Choices().entry_correct()
		# incorrectanswers = Choices().entry_incorrect()

		# # initialize the GameScript class
		# gamescript = GameScript()
		# # load the level description that matches the current level
		# gamescript.level_description('entry')

		# flag = True
		# user_input = raw_input("> ")
		# attempts = 1

		# # working while loop to check for correct and incorrect answers:
		# while flag:
		# 	if user_input in correctanswers:
		# 		nextlevel = Teller().start()
		# 		nextlevel
		# 		flag = False
		# 	elif user_input in incorrectanswers:
		# 		flag = False
		# 		gameover = Caught()
		# 		gameover()
		# 	elif attempts > 3:
		# 		gameover = Caught()
		# 		gameover()				
		# 	else:
		# 		print "Try again:\n"
		# 		user_input = raw_input("> ")
		# 		attempts = attempts + 1


class Teller(object):

	def start(self):
		# print "You're now at the bank teller"

		# Get game description for level teller
		gamescript = GameScript()
		gamescript.level_description('teller')

		# get choices/answers and assign the list to a variable correctanswers
		correctanswers = Choices().teller_correct()
		incorrectanswers = Choices().teller_incorrect()

		flag = True
		user_input = raw_input("> ")
		attempts = 1

		# working while loop to check for correct and incorrect answers:
		while flag:
			if user_input in correctanswers:
				nextlevel = BackOffice().start()
				nextlevel
				flag = False
			elif user_input in incorrectanswers:
				flag = False
				gameover = Caught()
				gameover()
			elif attempts > 3:
				gameover = Caught()
				gameover()				
			else:
				print "Try again:\n"
				user_input = raw_input("> ")
				attempts = attempts + 1


class BackOffice(object):

	def start(self):
		
		# Get game description for level teller
		# Get game description for level teller
		gamescript = GameScript()
		gamescript.level_description('back office')

		# get choices/answers and assign the list to a variable correctanswers
		correctanswers = Choices().backoffice_correct()
		incorrectanswers = Choices().backoffice_incorrect()

		flag = True
		user_input = raw_input("> ")
		attempts = 1

		# working while loop to check for correct and incorrect answers:
		while flag:
			if user_input in correctanswers:
				nextlevel = Vault()
				nextlevel.first_attempt()
				flag = False
			elif user_input in incorrectanswers:
				flag = False
				gameover = Caught()
				gameover()
			elif attempts > 3:
				gameover = Caught()
				gameover()				
			else:
				print "Try again:\n"
				user_input = raw_input("> ")
				attempts = attempts + 1


class Vault(object):
	# Guess the combination of the vault to enter and steal 
	# all the money in there.

	def next_vault_level(self, level):

		self.level = level

		if level == "second":
			Vault().second_attempt()
		elif level == "third":
			Vault().third_attempt()
		elif level == "success":
			"\nYES YOU'RE IN THE VAULT\n"
			Tunnel().start()

	def turn_vault_wheel(self, correct, nextlevel):

		self.correct = correct
		self.nextlevel = nextlevel

		turnwheel = raw_input("> ")
		flag = True
		attempt = 1

		while flag:
			if turnwheel in correct:
				flag = False
				Vault().next_vault_level(nextlevel)
			elif attempt < 2:
				print "try again"
				attempt = attempt + 1
				turnwheel = raw_input("> ")
			else:
				Caught()
		
	def first_attempt(self):

		print """\nYou arrived at the bank's vault, try to 
unlock the vault spin the wheel left or right\n"""

		attempt = Vault().turn_vault_wheel('right', 'second')


	def second_attempt(self):

		print "\nNice, second move left or right?\n"

		attempt = Vault().turn_vault_wheel('left', 'third')


	def third_attempt(self):

		print "\nGreat, one more turn... left or right?\n"

		attempt = Vault().turn_vault_wheel('right', 'success')


class Tunnel(object):

	def start(self):
		
		# Get game description for level tunnel
		gamescript = GameScript()
		gamescript.level_description('tunnel')

		# Get choices/answers and assign the list to a variable correctanswers
		correctanswers = Choices().tunnel_correct()
		incorrectanswers = Choices().tunnel_incorrect()

		flag = True
		user_input = raw_input("> ")
		attempts = 1

		# Working while loop to check for correct and incorrect answers:
		while flag:
			if user_input in correctanswers:
				nextlevel = Escape().the_end()
				nextlevel
				flag = False
			elif user_input in incorrectanswers:
				flag = False
				gameover = Caught()
				gameover()
			elif attempts > 3:
				gameover = Caught()
				gameover()				
			else:
				print "Try again:\n"
				user_input = raw_input("> ")
				attempts = attempts + 1


class Escape(object):
	# Class for the final scene of the game, when the user has
	# successfully escaped.

	def the_end(self):
		print "\nCongratulations, you successfully escaped with the money!\n"
		exit(0)


class Generator(object):
	'''Generator class is currently not being used to load the next level'''

	def nextlevel(self, level):
		# Initialize the Bank class 

		self.level = level

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

				levelvalue = levels[getnext]

				# print levelvalue
				Generator().loadnextlevel(levelvalue)


class StartGame(object):
	# class to start the game

	def load_areas(self):

		print "\n-----"

		print "\nBANK ROBBERY GAME"

		# initialize the Bank class 
		the_bank = Bank().bank_areas()
		# set the current level, this statement will return dict value 'entry'
		currentlevel = the_bank['level 0']

		# initialize and load the Level logic class
		Level()



# initialize the StartGame class and start the game:
# StartGame().load_areas()

# Vault().first_attempt()

Entry().answerloop('entry')
