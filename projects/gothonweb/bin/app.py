import web
from gothonweb import map

urls = (
	'/game', 'GameEngine',
	'/', 'Index',
)

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
		session.room = map.START
		web.seeother("/game")

class GameEngine(object):
	
	def GET(self):
		if session.room:
			return render.show_room(room=session.room)
		else:
			# why is this here? do you need it?
			return render.you_died()

	def POST(self):
		form - web.input(action=None)

		# there is a bug here, can you fix it?
		if session.room and form.action:
			session.room = session.room.go(form.action)

		web.seeother("/game")


if __name__="__main__":
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