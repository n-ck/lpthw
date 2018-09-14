# create a mapping of state to abbreviation
states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
	}

# create a basic set of states and some cities in them
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using the sate then cities dict
print '-' * 10
print "Michigan has: ", cities[states["Michigan"]]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print '-' * 10
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
	print "%s state is abbreviated %s and city %s" % (
		state, abbrev, cities[abbrev])

print '-' * 10
# safely get an abbreviation by state that might not be there
state = states.get('Texas', None)

if not state:
	print "Sorry, no Texas."

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is %s" % city


provincies = {
	'Z-H': 'Zuid-Holland',
	'N-H': 'Noord-Holland',
	'UT': 'Utrecht',
	'GR': 'Groningen',
}
steden = {
	'Z-H': 'Rotterdam',
	'N-H': 'Amsterdam',
	'UT': 'Utrecht',
	'GR': 'Groningen',
}

print provincies['Z-H']
print steden['UT']

# print all keys in provincies
for abbrev in provincies.items():
	print abbrev

# print all keys in provincies
for abbrev in provincies:
	print abbrev

#print all keys in provincies
for abbrev, states in provincies.items():
	print abbrev

#print all values in provincies
for abbrev in provincies:
	print(provincies[abbrev])

for abbrev, states in provincies.items():
	print steden[abbrev]

# print number of key-value pairs in the dictionary
print len(steden)

# add a new item to a dictionary
steden['N-B'] = "Breda"

print steden['N-B']
print len(steden)

# remove key value pair
del steden['N-B']
print len(steden)

# get() gets value of specified key
print steden.get('Z-H')

# update() add a new key-value pairs
steden.update({'N-B': 'Breda'})

print steden.keys()
print steden.values()
print steden.values()
