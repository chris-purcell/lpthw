from sys import argv

script, filename = argv

print "We're going to create %r and read it when we're done." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Creating the file..."
target = open(filename, 'w')

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to %r now." % filename

target.writelines([ "\n", line1, "\n", line2, "\n", line3, "\n"])

print "And finally, we close it and read it."
target.close()

target = open(filename)

print(target.read())
