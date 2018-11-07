import web

urls = (
	'/', 'Index',
	'/test', 'Test',
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class Index(object):
	def GET(self):
		# enter greeting in url as /?name=Nick
		greeting = web.input(name=None)
		return render.index(greeting = greeting.name)

class Test(object):
	def GET(self):
		message = "Test 123"
		return render.test(message = message)

if __name__=="__main__":
	app.run()