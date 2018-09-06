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

	# Create a list that just contains i
	numbers = [i]

	# for variable i in the numbers list:
	for i in numbers:
		# if i is smaller than top [given in the function]
		if i < top: 
			# print:
			print "At the top i is %d" % i
			
			# then increment i with the incr variable
			i = i + incr
			# and append the numbers list with the new i value
			numbers.append(i)

			# print the list and the value of i
			print "Numbers now: ", numbers
			print "At the bottom i is %d" % i

for_numbers(0, 10, 1)