
class GameScript():
	def game_level(self, level):
		self.level = level
		print level


	def level_description(self, level):

		self.level = level

		if level == "entry":
			print "\nYou're entering the bank"

		if level == "teller":
			print "\nYou're at the teller, try to not act suspicious"

		if level == "back office":
			print "\nYou made it to the back office"

		if level == "vault":
			print "\nYou're at the vault, try to get the right combination"

		if level == "tunnel":
			print "\nYou made it to the tunnel"