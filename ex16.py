from sys import argv

script, file = argv
#informing the user about the file name they've entered
print ("this is going to erase the file %r.", file)
print ("cancel the operation with shift c")
print ("press enter to continue")

input("?")

#opening the file with the name in the same path
print("opening file")
target = open(file, 'w')

#clearing the file
print("erasing file, type in 3 lines")
target.truncate

#getting 3 input lines
l1 = input("l1 -");
l2 = input("l2 -");
l3 = input("l3 -");

print("writing to file")

#creating a formatter combining paragraph and %r to specify how the variables will be printed
formatter = '''
%r
%r
%r
'''
#writing to file using the formatter and passing in the 3 lines
target.write(formatter % (l1, l2, l3))
#closing the file at the end
target.close()