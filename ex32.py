#looping thorugh lists and initializing lists in different ways
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
    print("This is count %d" % number)

for fruit in fruits:
    print("A fruit of type: %s" % fruit)

for i in change:
    print("I got %r" % i)

elements = []

#yes, it does print out element was 0~5
elements = range(0, 6)
 
for i in elements:
    print("Element was: %d" % i)

#more than appending, one can also pop a list