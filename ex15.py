#import the argv function from the sys module
from sys import argv

#give arguments script and filename to argv
script, filename = argv

#variable txt is assigned to open the filename from the second argument
txt = open(filename)

#line prints the name of the file, from the second argument
print "Here's your file %r:" % filename
#reads the content of the file as a string
print txt.read()

#print line
print "Type the filename again:"
#raw input where the user types the filename
file_again = raw_input("> ")

#variable txt_again is assigned to opening the file 
#based on the name typed into the prompt
txt_again = open(file_again)

#print the contents of the file as a string
print txt_again.read()