# Inside readline() is code that scans each byte of the file until it finds a \n character, 
# then stops reading the file to return what it found so far. 
# The file f is responsible for maintaining the current position in the file after each readline() call, 
# so that it will keep reading each line.

# The seek() function is dealing in bytes, not lines. 
# The code seek(0) moves the file to the 0 byte (first byte) in the file.



from sys import argv
script, input_file = argv


def print_all(f):
	print f.read()


def rewind(f):
	f.seek(0)


def print_a_line(line_count, f):
	print line_count, f.readline()



current_file = open(input_file)
print "First let's print the whole file :\n"
print_all(current_file)
print "Now let's rewind, kind of like a tape."
rewind(current_file)
print "Let's print three lines:"
current_line = 1
print_a_line(current_line, current_file)
current_line = current_line +1
print_a_line(current_line, current_file)
current_line = current_line +1
print_a_line(current_line, current_file)
