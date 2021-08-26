from sys import argv
#the shortest I can make is 7 lines
#getting parameters for the files to be written & read
script, fromfile, tofile = argv
#opening the two files, one will be rewritten
in_file = open(fromfile)
out_file = open(tofile, 'w')
#write with the content of the read file
out_file.write(in_file.read())
#close the two files
out_file.close()
in_file.close()