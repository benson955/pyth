from sys import argv

#getting files from prompt are more flexible as it can change based on runtime inputs,
#whereas having it as argv requires specification upfront

script, filename = argv

#program navigating to the filename from the current folder and reading it + assigning it to txt variable
txt = open(filename)

#reading out the file name again to the user using %r
print ("Here's your file %r:" % filename)
#displaying the contents of the txt file
print (txt.read())
#stop reading the file
txt.close()

#prompt for the file name, storing it to 'file_again'
print ("Type the filename again:")
file_again = (input("> "))

#read the file
txt_again = open(file_again)

#stop reading the file
txt_again.close()

#displaying the contents
print (txt_again.read())