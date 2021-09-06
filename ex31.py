print("You enter a dark room with two doors. Do you go through door #1 or door #2?")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake. What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")
    print("3. Take the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    elif bear == "3":
        print("You are now in possession of a bear, take good care of it.")
    else:
        print("Well, doing %s is probably better. Bear runs away."%bear)
    
elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")
    
    insanity = input("> ")
    
    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of a jello. good job!")
    else:
        print("The insanity roots your eyes into a pool of muck. Good job!")
    
elif door == "3":
    print("You have entered into the game expansion")
    print("You decide what happens to the bear")
    print("1. It turns into a frog.")
    print("2. It flies away.")
    
    choice = input("> ")
    
    if choice == "1" or choice == "2":
        print("How imaginative!")
    else:
        print("The sky is the limit.")

else:
    print("You stumble around and fall on a knife and die. Good job!")