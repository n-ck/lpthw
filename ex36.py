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

	decision = raw_input("save or invest: ")

	if decision == save:
		roi_save(dollars)
	elif decision == invest:
		roi_invest(dollars)
	else:
		kill("Whatever")

# def roi_save(dollars):
	# roilist = [1, 3, 5]

# def roi_invest(dollars):
	# roilist = [5, 10, 15]


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