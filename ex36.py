from sys import exit


def start():
	'''This function starts off the game'''

	print "This script calculates return on savings or investment"
	print "Enter the amount you want to save or invest"

	amount = raw_input("> ")
	dollars = int(amount)

	secondstep(dollars)


def secondstep(dollars):
	'''This function checks if the investment amount is enough'''

	if dollars < 500:
		kill("Save up more money.")
	else:
		saveorinvest(dollars)


def saveorinvest(dollars):
	'''This function decides if you want to save or invest'''

	print "Do you want to save or invest your money?"

	decision = raw_input("> ")

	if decision == "save":
		# print "You received 1% interest"
		# print dollars * 1.01
		choice = "save"
		selectyears(dollars, choice)
	elif decision == "invest":
		# print "You received 5% interest"
		# print dollars * 1.05
		choice = "invest"
		selectyears(dollars, choice)
	else:
		kill("Whatever")


def selectyears(dollars, choice):

	print "Choose the term in years"

	decision = raw_input("> ")
	years = int(decision)

	if years < 2:
		kill("Th term is too short")
	else:
		roicalculator(dollars, choice, years)


def compoundinterest(dollars, years, interest):
	'''Compound interest calculator formula, rounded down to 2 decimal points'''
	return float(str(round((dollars*(1 + interest)**((1 + interest)*years)), 2)))


def roicalculator(dollars, choice, years):

	interest = 0.01
	calcsavings = dollars*(1 + interest)**((1 + interest)*years)
	savings = float(str(round(calcsavings, 2)))
	calcinvestment = dollars*(1 + interest)**((1 + interest)*years)
	investment = float(str(round(calcinvestment, 2)))
	difference = investment - savings


	if choice == "save":
		print "Enter one or more interest rates"
		## Enter interest rates as a list [0.009, 0.01, 0.011]
		interests = raw_input("> ")
		interestlist = eval(interests)

		for interest in interestlist:

			print compoundinterest(dollars, years, interest)

			# print "Based on a %s percent interest rate," % (interest * 100)
			# print "You'd save %s" % savings
			# print "If invested with 10 interest you'd have: %s" % investment
			# print "The difference is: %s" % difference

		yearoptions(dollars, choice, years, interest)

	elif choice == "invest":
		print "Enter one or more interest rates"
		## Enter interest rates as a list [0.009, 0.01, 0.011]
		interests = raw_input("> ")
		interestlist = eval(interests)
		
		for interest in interestlist:

			print compoundinterest(dollars, years, interest)

			# print "Based on a %s percent interest rate," % (interest * 100)
			# print "Your roi would be %s" % investment
			# print "Saved with a 1 interest you'd have: %s" % savings
			# print "the difference is: %s" % (investment - savings)

		yearoptions(dollars, choice, years, interest)


def yearoptions(dollars, choice, years, interest):

	print "Do you want to calculate your interest for different years?"

	userinput = raw_input("> ")

	if userinput == "yes":

		print "For how which years do you wish to recalculate?"
		moreyears = raw_input("> ")
		moreyearlist = eval(moreyears)

		for additional in moreyearlist:

			print compoundinterest(dollars, additional, interest)

	else:
		kill("End.")

def kill(why):
	'''This function exits the game in terminal if you're dead'''
	print why, "Start over again"
	exit(0)


start()


"""
GAME PLANNING:

Calculate return on savings or investment

1. Enter dollar amount to invest or save
2. Pick if you choose to save or invest the money

If investment:
3. Enter investment interest rate
	3.1 if too low print: take more risk  - try again
	3.2 if too high print: this unrealistic - try again
4. Enter term in years
	4.1 if too low print: this too short - try again
	4.2 if too high print: this is way too high  - try again
5. Print return on investment and compare it to 
	adding the money to a savings account (1% interest)


If saving:
3. Enter savings interest rate
	3.1 if too low print: take more risk  - try again
	3.2 if too high print: this unrealistic - try again
4. Enter term in years
	4.1 if too low print: this too short - try again
	4.2 if too high print: this is way too high  - try again
5. Print return on savings and compare it to 
	adding the money to a investment account (3%, 5% and 10% interest)

6. Provide the option to run the program again

Additional options:
- Calculate for different terms (in years)
- Calculat for different investment/savings rates (in percentages)

"""