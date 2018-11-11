import web

urls = (
	'/hello', 'Index',
)

app = web.application(urls, globals())

render = web.template.render('templates/', base='base')

class Index(object):
	def GET(self):
		# enter greeting in url as /?name=Nick
		# greeting = web.input(name=None)
		# return render.index(greeting = greeting.name)

		form = web.input(name="Nobody", greet=None)

		if form.greet:
			greeting = "%s, %s" % (form.greet, form.name)
			return render.index(greeting = greeting)
		else:
			return "ERROR: greet is required."

		# greeting = "%s, %s" % (form.greet, form.name)

		# return render.index(greeting = greeting)

# class Test(object):
# 	def GET(self):
# 		message = "Test 123"
# 		return render.test(message = message)

if __name__=="__main__":
	app.run()