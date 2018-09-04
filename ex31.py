print "You enter a dark room with two doors. Do you go through door #1, #2 or #3?"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheese cake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."

	bear = raw_input("> ")

	if bear == "1":
		print "The bear eats your face off. Good job!"
	elif bear == "2": 
		print "The bear eats your legs off. Good job!"
	else:
		print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
	print "You stare into the endless abyss at Cthulhu's retina."
	print "1. Blueberries"
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."

	insanity = raw_input("> ")

	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jellow. Good job!"
	else:
		print "The insanity rots your eyes into a pool of muck. Good job!"

elif door == "3":
	 print "You won a brand new car, which one do you want?"
	 print "1. BMW M3"
	 print "2. Audi S7"
	 print "3. Mini Cooper"

	 car = raw_input("> ")

	 if car == "1":
	 	print "Congratulations on your new BMW"
	 elif car == "2":
	 	print "Why didn't you pick the BMW?"
	 elif car == "3":
	 	print "This is the wordst possible choice of these three cars."
	 else:
	 	print "No car for you"

else:
	print "You stumble around and fall on a knife and die. Good job!"