import time
numbers = [1, 2, 3, 356, 6, 7, 8, 34, 7, 356, 45]

def findInArr(tar, arr):
    occurences = []
    global starttime
    starttime = time.time()
    for i, n in enumerate(arr):
        if(n == tar):
            occurences.append(i)
    return occurences

print(findInArr(356, numbers))
print(time.time() - starttime)