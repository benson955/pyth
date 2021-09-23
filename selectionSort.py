list = input("Input me some list of numbers (w/ spaces in between) \n")
list = list.split(" ")
def ss(lst):
    for x in range(len(lst)):
        min = x
        for i in range(len(lst) - x):
            i = i + x
            if int(lst[min]) > int(lst[i]):
                min = i
        lst[min], lst[x] = lst[x], lst[min]
ss(list)
print(list)

#no worst or best case, have to loop through all anyways to check if any may be even smaller