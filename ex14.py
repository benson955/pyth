from sys import argv

#stating 2 additional args to be entered before running file
script, user_name, grade = argv
#specifying a string
prompt = 'enner something ay > '

#printing a string with 3 variables, followed up with % and the 3 accordingly
print ("Hi %s from grade %s, I'm the %s script." % (user_name, grade, script))
print ("I'd like to ask you a few questions.")
print ("Do you like me %s?" % user_name)
#input with the string prompt inside as the message
likes = input(prompt)

#string with 1 variable
print ("Where do you live %s?" % user_name)
#input with the string prompt inside as the message
lives = input(prompt)

print ("What kind of computer do you have?")
#input with the string prompt inside as the message
computer = input(prompt)

#printing a paragraph with 3 variables inside
print ("""
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer.  Nice.
""" % (likes, lives, computer))