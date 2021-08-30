from sys import argv
#taking in two arguments to run the file
script, input_file = argv

#defining a printall function to print the file content
def print_all(f):
    print (f.read())

#defining a rewind function to get to the first letter of the file content
def rewind(f):
    f.seek(0)

#defining a print a line function with the int of line count and file to print the file at the given line
def print_a_line(line_count, f):
    print (line_count, f.readline())

#open the file and set it to var current file
current_file = open(input_file)

#printing and switching to new line
print ("First let's print the whole file:\n")

#calling the function printall and passing in the file
print_all(current_file)

print ("Now let's rewind, kind of like a tape.")

#calling rewind function and passing in the file
rewind(current_file)

print ("Let's print three lines:")

#initiated as 1
current_line = 1
#printing line 1 of the file
print_a_line(current_line, current_file)
#incrementing by 1, now 2
current_line += 1
#printing line 2 of the file
print_a_line(current_line, current_file)
#increment again, now 3
current_line += 1
#printing line 3 of the file
print_a_line(current_line, current_file)