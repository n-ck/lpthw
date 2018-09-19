## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

## Dog is-a animal
class Dog(Animal):

	def __init__(self, name):
		## ??
		self.name = name


## Cat is-a animal
class Cat(Animal):

	def __init__(self, name):
		## ??
		self.name = name

## ??
class Person(object):

	def __init__(self, name):
		## ??
		self.name = name

		## Person has-a pet of some kind
		self.pet = None

## ??
class Employee(Person):

	def __init__(self, name, salary):
		## ?? hmm wat is this strange magic
		super(Employee, self).__init__(name)
		## ??
		self.salary = salary

## Fish is-a object
class Fish(object):
	pass

## Salmon is-a Fish
class Salmon(Fish):
	pass

## Halibut is-a fish
class Halibut(Fish):
	pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet called Satan
mary.pet = satan

## frank is-a employee and has-a name "Frank" and has-a 120k salary
frank = Employee("Frank", 120000)

## an Employee is a Person and the person Frank has-a pet called Rover
frank.pet = rover

## flipper is-a fish
flipper = Fish()

## crouse is-a salmon
crouse = Salmon()

## harry is-a halibut
harry = Halibut()
