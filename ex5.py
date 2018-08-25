my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74.0 # inches
my_weight = 180.0 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavey." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d and %d I get %d" % (
	my_age, my_height, my_weight, my_age + my_height + my_weight)

print "Testing this format character out %r" % my_name

height_cm = my_height * 2.54
weight_kg = my_weight * 0.453

print "My weight in kilos is %dkg" % weight_kg
print "My height in cm is %dcm" % height_cm