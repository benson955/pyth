#the input function gets input from the user
#asing with a printing prompt and getting input
print("What grade are you in?"),
grade = input()
print("Where do you live?"),
location = input()
print("How happy are you?"),
happiness = input()

#printing a whole string with the 3 variables
print("You are in grade %r, living in %r and am %r" % (grade, location, happiness))

#in writing 6'2, single quotes are escaped with a backslack before it \'