class Scene(object):

	def enter(self):
		pass

# The engine runs a map full of rooms or scenes
# Each room will print its own description when the player enters it
# and then tell the engine what room to run next out of the map.
class Engine(object):

	def __init__(self, scene_map, game_start):
		self.scene_map = scene_map
		self.game_start = game_start

	def play(self):
		print self.scene_map
		print self.game_start

		print """\nYou start in the central corridor of the spaceship
		There is a hammer and a lasergun on the ground
		there is a closed door in front of you,
		how do you continue?"""

		# scenes = ['Central Corridor', 
		# 		  'Laser Weapon Armory',
		# 		  'The Bridge',
		# 		  'Escape Pod']

		# for scene in scenes:
		# 	print scene

		# print "Enter your choice:\n"
		firstscene = raw_input("> ")

		if "lasergun" in firstscene:
			print "you opened the door"
			next_scene = Map('central corridor')
			next_scene.opening_scene()
		elif "hammer" in firstscene:
			print "the door won't open"
		else:
			yourdead = Death()
			yourdead.enter()			

		# for chosenscene in scenes:

		# 	if firstscene == chosenscene:
		# 		yourchoice = chosenscene
		# 		print "Continue to the next level in %s" % yourchoice

		# # initialize the Map class
		# gamemap = Map(yourchoice)
		# # load the opening_scene function of the Map class
		# gamemap.opening_scene()


# This is when the player dies and should be something funny
class Death(Scene):

	def enter(self):
		print "Game Over!!!"
		exit(0)

# This is the starting point
class CentralCorridor(Scene):

	def enter(self):
		print "\nYou entered the Central Corridor"
		print "\nType something:"

		next_scene = raw_input("> ")

		if next_scene != "":
			laserweapon = LaserWeaponArmory()
			laserweapon.enter()

# The second scene (after the Central Corridor)
class LaserWeaponArmory(Scene):

	def enter(self):
		print "You're now in the Laser Weapon Armory"
		print "\nType something:"

		next_scene = raw_input("> ")

		if next_scene != "":
			thebridge = TheBridge()
			thebridge.enter()

# This is the third scene
class TheBridge(Scene):

	def enter(self):
		print "You entered the Bridge"

		next_scene = raw_input("> ")

# Final scene, escape through the Escape Pod
class EscapePod(Scene):

	def enter(self):
		print "Congratulations you escaped through the Escape Pod!"
		print "This is the end of the game!"

class Map(object):

	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_scene(self, scene_name):
		pass

	def opening_scene(self):
		# initialize the CentralCorridor class
		centralcorridor = CentralCorridor()
		# load the enter function of the CentralCorridor class
		centralcorridor.enter()

# a_map = Map('central_corridor')
# a_game = Engine(a_map)
# a_game.play()

startgame = Engine('centralcorridor', 'yes')
startgame.play()
