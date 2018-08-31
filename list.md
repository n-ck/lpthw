# List of all things Python 

## Comments

```# comment
'''multiline comment''' 
"""multiline comment"""
```

## Variables

```
cars = 10  
car = "bmw"  
half_car = 0.5 # Float  
```

## Print

```
print "Enter string here"
or 
car = "audi"
print car
or
print """
Enter your multiline string here
"""
```
  
## format characters
```
%s - string  
%d - integer decimal  
%r - raw string (used for debugging)  
```

Usage example:
```
print "Hi %s" % username
print "Hi %s I'm the %s script" % (username, script)
```
  
More about [format characters](https://docs.python.org/2.4/lib/typesseq-strings.html)

### Escape sequences
```
\n - new line in a string  
\t - tab  
\ - Use backslash to escape quotes within a string  
\r - takes cursor to beginning of line (and overwrites it) 
```

## Raw input
Use raw_input() to ask a user to input something in the terminal.
```
raw_input()  
raw_input("Write instructions here: )  
var = raw_input() - assigns raw input to a variable  
```

## argv
```
from sys import argv
script, first, second, third = argv  

running this in the terminal:
python ex13.py first second third

passes the values entered in the terminal as values for the arguments (variables) in argv
```

## Reading files
```
open(filename) - creates object of the file, takes filename as a parameter  
open(filename, w) - takes filename parameter and open it in 'writemode' (r, 'readmode' is the default)
.read() - returns the contents of a file
.readline() - Reads jus tone line of a text file
.truncate() - Empties the file 
.write(stuff) - Overwrite the content of a file 
.close() - Closes the filename

len() - gets the length of a string you pass and returns it as a number
```

## Functions

```
def functionname(arg1, arg2):
	print "Hello %s, do stuff here %s" % (arg1, arg2)
```

*Left off with the Python list at exercise 27*

*Left off at page 83/101[PDF] - Exercise 24*