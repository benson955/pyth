# a class is just a type, a dir returns all possible methods and values for that specific object
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there's not 10 things in that list, let's fix that.")

#this function splits the single string based on spaces ' '
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    #gets and stores the last one off of more_stuff
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    #add that to the list
    stuff.append(next_one)
    #get the length of the list
    print("There's %d items now." % len(stuff))

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
#join with spaces ' '
print(' '.join(stuff))
#join with '#'
print('#'.join(stuff[3:5]))