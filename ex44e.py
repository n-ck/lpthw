class Other(object):

	def override(self):
		print "OTHER override()"

	def implicit(self):
		print "OTHER implicit()"

	def altered(self):
		print "OTHER altered()"


class Child(object):

	def __init__(self):
		self.other = Other()

	def implicit(self):
		self.other.implicit()

	def override(self):
		print "CHILD override()"

	def altered(self):
		print "CHILD, BEFORE OTHER altered()"
		self.other.altered()
		print "CHILD, AFTER OTHER altered()"

son = Child()

son.implicit()
son.override()
son.altered()


## Class Inheritance

class Parent(object):

	def lastname(self, lastname):
		self.lastname = lastname
		print self.lastname

class Child(Parent):

	def firstname(self, firstname):
		self.firstname = firstname
		print self.firstname


name = Child()

name.firstname('First')
name.lastname('Last')

## Class Composition

class Brand(object):

	def brandname(self, make):
		self.make = make
		print self.make

class Car(object):

	def __init__(self):
		self.brand = Brand()

	def carbrand(self):
		self.brand.brandname()
		
	def cartype(self, carmodel):
		self.carmodel = carmodel
		print self.carmodel

name = Car()

name.carbrand('BMW')
name.cartype('sedan')

