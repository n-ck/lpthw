'''
def my_numbers(i, top, incr):

	numbers = []

	while i < top:
		print "At the top i is %d" % i
		numbers.append(i)

		i = i + incr
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

	print "The numbers: "

	for num in numbers:
		print num


my_numbers(0, 10, 2)
'''

## The same function using for loops

def for_numbers(i, top, incr):

	numbers = []

	for i in numbers:
		if i < 12: 
			print "At the top i is %d" % i
			numbers.append(i)

			i = i + incr
			print "Numbers now: ", numbers
			print "At the bottom i is %d" % i

for_numbers(0, 10, 2)