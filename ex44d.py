class Parent(object):

	def override(self):
		print "PARENT override()"

	def implicit(self):
		print "PARENT implicit()"

	def altered(self):
		print "PARENT altered()"

class Child(Parent):

	def override(self):
		print "CHILD override()"

	def altered(self):
		print "CHILD, BEFORE PARENT altered()"
		super(Child, self).altered()
		print "CHILD, AFTER PARENT altered()"

# initializes the Parent class:
dad = Parent()
# initializes the Child class:
son = Child()

# Prints the implicit function of the Parent class
dad.implicit()
# Prints the implicit function of the Parent class
son.implicit()

# Prints the override function of the Parent class
dad.override()
# Prints the override function of the Child class
son.override()

# Prints the altered function of the Parent class 
dad.altered()

# Prints the Child altered function
son.altered()