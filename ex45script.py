
class GameScript():
	def game_level(self, level):
		self.level = level
		print level


	def level_description(self, level):

		self.level = level

		if level == "entry":
			print "You're entering the bank"

		if level == "teller":
			print "You're at the teller, try to not act suspicious"

		if level == "back office":
			print "You made it to the back office"

		if level == "vault":
			print "You're at the vault, try to get the right combination"

		if level == "tunnel":
			print "You made it to the tunnel"