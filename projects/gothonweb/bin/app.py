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

		print session.room

	def POST(self):
		form = web.input(action=None)

		web.config._session = session

		# deathlist = {"central_corridor": "You're floating in space infinitely",
		# 			 "laser_weapon_aromory": "You're never unlocking a weapon, you die!",
		# 			 "the_bridge": "You fall of the bridge and crush your skull",
		# 			 "escape_pod": "The escape pod burns out completely, you're dead...",
		# 			}

 	# 	correctanswers = {"laser_weapon_armory": "tell a joke", 
 	# 	 				  "the_bridge": "0132", 
 	# 	 				  "escape_pod": "slowly place the bomb", 
 	# 	 				  "the_end_winner": "2"
 	# 	 				  }

		# flag = True

 	# 	while flag:

		# 	if form.action == "tell a joke":
		# 		session.room = map.laser_weapon_armory
		# 		return render.show_room(room=session.room)
		# 		print session.count
		# 		flag = False

		# 	elif session.count == 3:
		# 		for x, y in deathlist.items():
		# 			if key == x:
		# 				return render.you_died(reason=y)
		# 	else:
		# 		session.count = session.count + 1
		# 		session.room = map.central_corridor
		# 		return render.show_room(room=session.room)
		# 		flag = False	 				


		### Working code:

		if form.action == "tell a joke":
			session.room = map.laser_weapon_armory
			# print session.room.name
			return render.show_room(room=session.room)

		elif form.action == "0132":
			session.room = map.the_bridge
			return render.show_room(room=session.room)

		elif form.action == "slowly place the bomb":
			session.room = map.escape_pod
			return render.show_room(room=session.room)

		elif form.action == "slowly place the bomb":
			session.room = map.escape_pod
			return render.show_room(room=session.room)	

		elif form.action == "2":
			session.room = map.the_end_winner
			return render.the_end(room=session.room)

		else:
			# for key, value in deathlist.items():
			# 	if key == session.room:
			return render.you_died()
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