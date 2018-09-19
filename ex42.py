## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

## Dog is-a animal
class Dog(Animal):

	def __init__(self, name):
		## Dog has-a nam
		self.name = name


## Cat is-a animal with an __init_ that takes self and name parameters
class Cat(Animal):

	def __init__(self, name):
		## Cat has-a name
		self.name = name

## Person is-a object with an __init__ that takes self and name parameters
class Person(object):

	def __init__(self, name):
		## Person has-a name
		self.name = name

		## Person has-a pet of some kind
		self.pet = None

## ??
class Employee(Person):

	def __init__(self, name, salary):
		## ?? hmm wat is this strange magic
		## refers to the init function of the inherited class (the Person class) without having to mention
		## the class name, if the class Person changed to People the super line would still work.
		super(Employee, self).__init__(name)
		## Employee has a salaray
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

## rover is-a Dog - rover is an instance of Dog
rover = Dog("Rover")

## satan is-a Cat - satan is an instance of Cat
satan = Cat("Satan")

## mary is-a Person - mary is an instance of Person
mary = Person("Mary")

## mary has-a pet called Satan
mary.pet = satan

## frank is-a employee and has-a name "Frank" and has-a 120k salary
## frank is an instance of Employee
frank = Employee("Frank", 120000)

## an Employee is a Person and the person Frank has-a pet called Rover
frank.pet = rover

## flipper is-a fish - set flipper to an instance of Fish
flipper = Fish()

## crouse is-a salmon - set crouse to an instance of Salmon
crouse = Salmon()

## harry is-a halibut - set harry to an instance of Halibut
harry = Halibut()
