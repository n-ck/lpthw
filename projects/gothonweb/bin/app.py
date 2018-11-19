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
								  initializer={'room': None})
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

		# session.room = map.laser_weapon_armory
		# render.show_room(room=session.room)

		## there is a bug here, can you fix it?

		# print session.room

		# for key,value in session.room.items():
		# 	if value == generic_death:
		# 		return render.show_room(session.room)
		# 	else:
		# 		session.room = map.value
		# 		return render.show_room(room=session.room)

		if form.action == "tell a joke":
			print form.action
			# print session.room 
			# session.room = map.Room.paths
			# print session.room.paths

			## Attempt to print the current session:
			# x = base64.b64decode(open("sessions/e5f756478a4a324b84deb8535015ea88b02d9629").read())
			# y = pickle.loads(x)
			# print y

			session.room = map.laser_weapon_armory
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
			return render.you_died()

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