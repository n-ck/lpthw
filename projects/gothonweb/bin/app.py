import web
from gothonweb import map
import pickle
import base64

urls = (
	'/game', 'GameEngine',
	'/the_end', 'GameEngine',
	'/', 'Index',
)

## Run this in terminal before trying to run the game:
#export PYTHONPATH=$PYTHONPATH:.

app = web.application(urls, globals())

# little hack so that debug mode works with sessions
if web.config.get('_sessions') is None:
	store = web.session.DiskStore('sessions')
	session = web.session.Session(app, store, 
								  initializer={'room': None,
								  			   'current_level': 'central_corridor',
								  			   'points': 0,
								               'count': 0,
								               })
	web.config._session = session
else:
	session = web.config._session

render = web.template.render('templates/', base="base")


class Index(object):
	def GET(self):

		# this is used to "setup" the session with starting values
		## ads the map.START room (central_corridor) to the session dictionairy
		session.room = map.START
		web.seeother("/game")

class GameEngine(object):
	
	def GET(self):

		session.room = map.START

		if session.room:
			return render.show_room(room=session.room)
		else:
			# why is this here? do you need it?
			return render.you_died()


	def POST(self):
		form = web.input(action=None)

		web.config._session = session

		session.current_level = "central_corridor"
		# print str(session.count)

		deathlist = {"Central Corridor": "You're floating in space infinitely",
					 "Laser Weapon Armory": "You're never unlocking a weapon, you die!",
					 "The Bridge": "You fall of the bridge and crush your skull",
					 "Escape Pod": "The escape pod burns out completely, you're dead...",
					}
		
		if form.action in map.central_corridor.correct or map.central_corridor.incorrect:

			session.room = map.central_corridor

			if form.action in map.central_corridor.correct:
				session.room = map.laser_weapon_armory
				session.current_level = "laser_weapon_armory"
				print str(session.current_level)
				return render.show_room(room=session.room)
			else:
				print session.room.name
				for key, value in deathlist.items():
					if key == session.room.name:
						reason = value
						return render.you_died(dead=reason)

		if form.action in map.laser_weapon_armory.correct or map.laser_weapon_armory.incorrect:

			session.room = map.laser_weapon_armory

			if form.action in map.laser_weapon_armory.correct:
				session.room = map.the_bridge
				session.current_level = "the_bridge"
				print str(session.current_level)
				return render.show_room(room=session.room)
			else:
				print session.room.name
				for key, value in deathlist.items():
					if key == session.room.name:
						reason = value
						return render.you_died(dead=reason)


		### Working code:

		# if form.action == "tell a joke":
		# 	session.room = map.laser_weapon_armory
		# 	# session.count += 1
		# 	session.current_level = "laser_weapon_armory"
		# 	print str(session.current_level)
		# 	return render.show_room(room=session.room)

		# elif form.action == "0132":
		# 	session.room = map.the_bridge
		# 	# session.count += 1
		# 	session.current_level = "the_bridge"
		# 	print str(session.current_level)
		# 	return render.show_room(room=session.room)

		# elif form.action == "slowly place the bomb":
		# 	session.room = map.escape_pod
		# 	# session.count += 1
		# 	session.current_level = "escape_pod"
		# 	print str(session.current_level)
		# 	return render.show_room(room=session.room)

		# elif form.action == "2":
		# 	session.room = map.the_end_winner
		# 	# session.count += 1
		# 	session.current_level = "the_end_winner"
		# 	print str(session.current_level)
		# 	return render.the_end(room=session.room)

		# else:
		# 	flag = True
		# 	while flag:
		# 		for key, value in deathlist.items():
		# 			if key == str(session.current_level):
		# 				reason = value
		# 				return render.you_died(dead=reason)
		# 				flag = False
				# else:
				# 	reason = "You died, bummer!"
				# 	return render.you_died(dead=reason)

			# if session.current_level == "central_corridor":
			# 	reason = "You're floating in space infinitely"
			# 	return render.you_died(dead=reason)



			# for key, value in deathlist.items():
			# 	if key == session.room:
			# return render.you_died()
			# session.room = map.generic_death
			# return render.you_died(room=session.room)

		# web.seeother("/game")


if __name__=="__main__":
	app.run()


# render = web.template.render('templates/', base='base')

# class Index(object):
# 	def GET(self):
# 		return render.hello_form()

# 	def POST(self):
# 		form = web.input(name="Nobody", greet="Hello")
# 		greeting = "%s, %s" % (form.greet, form.name)
# 		return render.index(greeting = greeting)

		# enter greeting in url as /?name=Nick
		# greeting = web.input(name=None)
		# return render.index(greeting = greeting.name)

		# form = web.input(name="Nobody", greet=None)

		# if form.greet:
		# 	greeting = "%s, %s" % (form.greet, form.name)
		# 	return render.index(greeting = greeting)
		# else:
		# 	return "ERROR: greet is required."

		# greeting = "%s, %s" % (form.greet, form.name)

		# return render.index(greeting = greeting)

# class Test(object):
# 	def GET(self):
# 		message = "Test 123"
# 		return render.test(message = message)

# if __name__=="__main__":
# 	app.run()