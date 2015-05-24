from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying %s to %s" % (from_file, to_file)

indata = open(from_file).read()

print "The input file is %d bytes long" % len(indata)

out_file = open(to_file, 'w')
out_file.write(indata)

print "All done!"

out_file.close()
