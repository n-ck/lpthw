from sys import argv

script, filename = argv

openfile = open(filename)

print "\nHere are the contents of the file %s : \n" % filename
print openfile.read()