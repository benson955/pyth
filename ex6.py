#define var, init @ 10
types_of_people = 10
#defining string x
x = f"There are {types_of_people} types of people."

#word vars named after their content
binary = "binary"
do_not = "don't"
#defining string y
#STRING INSIDE STRING x2
y = f"Those who know {binary} and those who {do_not}."

#printing the two string vars
print(x)
print(y)

#outputting STRING INSIDE STRING x2
print(f"I said: {x}")
print(f"I also said: '{y}'")

#expressing not funny as a boolean
hilarious = False
#defining string "joke_evaluation"
joke_evaluation = "Isn't that joke so funny?! {}"

#printing and adding var 'hilarious' inside the brackets in string 'joke_evaluation'
print(joke_evaluation.format(hilarious))

#defining two strings w and e
w = "This is the left side of..."
e = "a string with a right side."

#printing the sum of the two strings, essentially adding the characters together
print(w + e)