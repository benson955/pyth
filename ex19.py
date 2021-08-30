#defining a function taking in two numbers, and having it operate by printing a series of strings using the two inputs
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print ("You have %d cheeses!" % cheese_count)
    print ("You have %d boxes of crackers!" % boxes_of_crackers)
    print ("Man that's enough for a party!")
    print ("Get a blanket.\n")

#printing and calling on the function passing in 20 and 30 for the two variables
print ("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

#defining two variables storing two numbers
print ("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

#calling the the function passing in the numbers stored as variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#passing in numbers with operations, which will be executed as the final numbers
print ("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

#passing in both the variables and added number using mathematical operations
print ("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def saytheNumber(number1, number2):
    print("this is your number 1", number1)
    print("this is your number 2", number2)

#passing two numbers directly
saytheNumber(1, 2)
#passing in two numbers with math addition and subtraction
saytheNumber(1 + 1, 2 - 1)
#passing in with math divisions
saytheNumber(12 / 6, 2 / 2)
#passing in two multiplications
saytheNumber(1 * 8, 2 * 5)
#defining two variables
n1 = 5
n2 = 10
#passing in the two variables
saytheNumber(n1, n2)
#passing in addition and subtraction with the two variables
saytheNumber(n1 + 23, n2 - 1)
#passing in division with the two variables
saytheNumber(n1 / 5, n2 / 2)
#passing in multiplication with two variables
saytheNumber(n1 * 4, n2 * 8)
#performing operations with only variables
saytheNumber(n1 + n2, n2 + n1)
saytheNumber(n1 - n2, n2 - n1)