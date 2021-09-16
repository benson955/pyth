list = input("Input me some list \n")
list = list.split(" ")
def BubSort(lst):
    for x in range(len(lst)):
        for i in range(len(lst) - 1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
BubSort(list)
print(list)
#no space complexity, no overhead needing to be stored in new variables (direct swap)
#always the same due to for loop nature, range * range - 1 comparisons
#unstable for higher amounts of items