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

def roicalculator(dollars, choice, years):

	savings = dollars*(1.01)**(1.01*years)
	investment = dollars*(1.10)**(1.10*years)

	if choice == "save":
		print "Based on a 1% interest rate,"
		print "You'd save %s" % savings
		print "If you invested the money you would have %s" % investment
	elif choice == "invest":
		print "Based on a 10% interest rate,"
		print "Your roi would be %s" % investment
		print "If you saved the money you would have %s" % savings

def roi_save(dollars):
	'''This function calulcates roi on savings'''
	roilist = [1.01, 1.03, 1.05]

	for roi in roilist:
		print dollars * roi


def roi_invest(dollars):

	roilist = [1.05, 1.1, 1.15]

	for roi in roilist:
		print dollars * roi


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