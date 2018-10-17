
class GameScript():
	def game_level(self, level):
		self.level = level

	def level_description(self, level):

		self.level = level

		print "\n-----"

		text = {
				"entry": """\nYou arrived at the bank, ready to rob the contents 
of the vault, an estimated $25 million. 
You enter the bank cautious and insuspiciously, 
\nWhat is your next move...?\n""",

				"teller": """\nYou're at the teller, try to not act suspicious
Ask for information about opening a bank account,
but don't fill out an application right away!
\nAfter getting the information, 
make an excuse to use the bathroom...\n""",

				"back office": """\nGreat on your way to the bathroom you sneak 
into the back office and hide in the janitors closet. 
You come out after the bank closes and all bank employees left. The laser 
alarm system is on, you have to avoid the alarm from going of while you 
have to disarm the alarmsystem temporarily...\n""",

				"tunnel": """Awesome, you made it to the tunnel, you started
digging the tunnel from the other side months ago, now it's time for the last
step. What are you doing next...?\n"""

		}

		for key in text:
			if level == key:
				print text[key]