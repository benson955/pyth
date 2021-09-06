people = 9
cars = 41
buses = 99999999
#if runs on condition, else runs on the lack of condition, elseif runs if only another condition is met on top of the lack of condition
#initial condition
if cars > people and buses < cars:
    print("We should take the cars.")
#if either initial condition isnt met, yet meets this condition
elif cars < people:
    print("We should not take the cars.")
#catch all other cawses
else:
    print("We can't decide.")
#initial condition
if buses > cars:
    print("That's too many buses.")
#not initial but meets this condition
elif buses < cars:
    print("Maybe we could take the buses.")
#catach all
else:
    print("We still can't decide.")
#initial condition
if people > buses:
    print("Alright, let's just take the buses.")
else:
    print("Fine, let's stay home then.")
