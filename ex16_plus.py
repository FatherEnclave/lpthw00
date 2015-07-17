#Line 2 imports a module or library, in this case system imports argument variables
from sys import argv

#This line unpacks the variables script and filename
script, filename = argv

#8-10 will print what it says and then tells the filename from above
print "We're going to erase %r." %filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
#asks if you want to continue or cancel
raw_input("?")
#print + creates the variable 'target' which will open the filename variable specified earlier.
print "Opening the file..."
target = open(filename, 'w')

#print + truncates the target == erases all the content of the filename file.
print "Truncating the file. Goodbye!"
target.truncate()
#21-37 prints + asks for new content in the file you just erased which will become lines 1 2 and 3 and then close.
print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()

