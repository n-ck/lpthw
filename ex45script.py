
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
				"entry": "\nYou're entering the bank",
				"teller": "\nYou're at the teller, try to not act suspicious"

		}

		for key in text:
			if level == key:
				return text[key]