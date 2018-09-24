class Scene(object):

	def enter(self):
		pass

class Engine(object):

	def __init__(self, scene_map, game_start):
		self.scene_map = scene_map
		self.game_start = game_start

	def play(self):
		print self.scene_map
		print self.game_start

		print "\nChoose one of the following rooms to continue:\n"

		scenes = ['Central Corridor', 
				  'Laser Weapon Armory',
				  'The Bridge',
				  'Escape Pod']

		for scene in scenes:
			print scene

		print "Enter your choice:\n"
		firstscene = raw_input("> ")

		for chosenscene in scenes:

			if firstscene == chosenscene:
				yourchoice = chosenscene
				print "Continue to the next level in %s" % yourchoice

				gamemap = Map(yourchoice)
				gamemap.opening_scene()

			# 	yourdead = Death()
			# 	yourdead.enter()

class Death(Scene):

	def enter(self):
		print "Game Over!!!"
		exit(0)

class CentralCorridor(Scene):

	def enter(self):
		print "\nYou entered the Central Corridor"

class LaserWeaponArmory(Scene):

	def enter(self):
		pass

class TheBridge(Scene):

	def enter(self):
		pass

class EscapePod(Scene):

	def enter(self):
		pass

class Map(object):

	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_scene(self, scene_name):
		pass

	def opening_scene(self):
		centralcorridor = CentralCorridor()
		centralcorridor.enter()

# a_map = Map('central_corridor')
# a_game = Engine(a_map)
# a_game.play()

startgame = Engine('centralcorridor', 'yes')
startgame.play()
