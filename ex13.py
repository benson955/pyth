#the error explains there arent enough values to unpack.
#this is because the code instructed the program to look for _ amount of values, finding none
from sys import argv

#specifying 2 additional required variables
script, first, second = argv

#printing strings with the variables follow behind it
print ("The script is called:", script)
print ("Your first variable is:", first)
print ("Your second variable is:", second)

#getting another variable from runtime input
third = input("what is your third?")

#printing the string with variable
print ("Your third variable is:", third)