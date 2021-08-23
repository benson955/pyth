#the error explains there arent enough values to unpack.
#this is because the code instructed the program to look for _ amount of values, finding none
from sys import argv

script, first, second = argv

print ("The script is called:", script)
print ("Your first variable is:", first)
print ("Your second variable is:", second)

third = input("what is your third?")

print ("Your third variable is:", third)