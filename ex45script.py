
class GameScript():
	def game_level(self, level):
		self.level = level

	def level_description(self, level):

		self.level = level

		## Get level text based on if else statements:

		# if level == "entry":
		# 	print "\nYou're entering the bank"

		# if level == "teller":
		# 	print "\nYou're at the teller, try to not act suspicious"

		# if level == "back office":
		# 	print "\nYou made it to the back office"

		# if level == "vault":
		# 	print "\nYou're at the vault, try to get the right combination"

		# if level == "tunnel":
		# 	print "\nYou made it to the tunnel"


		## Get level text based on a dictionary:

		text = {
				"entry": """\nYou arrived at the bank, ready to rob the contents of their vault, 
							\nan estimated $25 million. You enter the bank cautious and inauspiciously, 
							\nwhat is your next move...?\n""",

				"teller": "\nYou're at the teller, try to not act suspicious",

				"back office": """Great you sneak into the back office and hide in the janitors closet. 
								You come out after the bank closes and all bank employees left. The laser 
								alarm system is on, you have to avoid the alarm from going of while you 
								have to disarm the alarmsystem temporarily..."""


		}

		for key in text:
			if level == key:
				print text[key]



# If bathroom:
# You enter the lobby, wait in line, then go to the bathroom and hide in one of the ac vents in the bathroom till the bank closes down.

# If back office:

# If smokebomb:
# Great you can see the laser detector streams now and can manouver through them, go to the main alarm system and disarm it.

# If flower:
# You throw flower in the air to see the lasers, now you can mover through the laser detectors.

# Security guard: