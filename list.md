# List of all things Python 

### Comments

```# comment
'''multiline comment''' 
"""multiline comment"""
```
  
### format characters  
%s - string  
%d - integer decimal  
%r - raw string (used for debugging)  

Usage example:
```
print "Hi %s" % username
print "Hi %s I'm the %s script" % (username, script)
```
  
More about [format characters](https://docs.python.org/2.4/lib/typesseq-strings.html)

4.0 floating point number

### Escape sequences

\n - new line in a string  
\t - tab  
\ - Use backslash to escape quotes within a string  
\r - takes cursor to beginning of line (and overwrites it)  

## Raw input 
Use raw_input() to ask a user to input something in the terminal.

raw_input()  
raw_input("Write instructions here: )  
var = raw_input() - assigns raw input to a variable  

## argv

from sys import argv
script, first, second, third = argv  

python ex13.py first second third

## Reading files

open(filename) - creates object of the file, takes filename as a parameter  
open(filename).read() - returns the contents of the file  
open(filename, w) - takes filename parameter and open it in 'writemode' (r, 'readmode' is the default)  
.truncate() - Truncates the file size (shorten by cutting off)  
.write() - Overwrite the content of a file  

*Left off with the Python list at exercise 17*

### Functions


*Left off at page 83/101[PDF] - Exercise 24*