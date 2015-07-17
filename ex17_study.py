#Imports from sys, arguments variables, and os.path, exists.
from sys import argv
from os.path import exists
#These are the argument variable functions, script is mandatory, from_file and to_file are user defined.
script, from_file, to_file = argv
#for user
print "Copying from %s to %s" %(from_file, to_file)

#we could do these two on one line too, how? use, ; to make 2 lines of code 1
in_file = open(from_file) ; indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()
