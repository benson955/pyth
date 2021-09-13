import time
numbers = [1, 2, 3, 356, 6, 7, 8, 34, 7, 356, 45]

def findInArr(tar, arr):
    end = len(arr) - 1
    offs = 0
    global starttime
    starttime = time.time()
    while offs < end / 2:
        if arr[offs] == tar:
            return offs
        if arr[end - offs] == tar:
            return end - offs
        offs += 1
    return "false"

print(findInArr(356, numbers))
print(time.time() - starttime)
# 0.0009 sec vs 0.003 on linearsearch