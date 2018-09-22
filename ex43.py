class Scene(object):

	def enter(self):
		pass

class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map

	def play(self):
		firstscene = raw_input("> ")
		if firstscene != "":
			exit()

class Death(Scene):

	def enter(self):
		pass

class CentralCorridor(Scene):

	def enter(self):
		pass

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
		pass

	def next_scene(self, scene_name):
		pass

	def opening_scene(self):
		pass

# a_map = Map('central_corridor')
# a_game = Engine(a_map)
# a_game.play()

startgame = Engine('centralcorridor')
startgame.play()
