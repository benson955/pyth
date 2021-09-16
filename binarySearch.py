import time
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def findInArr(tar, arr):
    ind = 0
    end = len(arr) - 1

    while ind <= end:
        mid = (ind + end) // 2
    
        if(arr[mid] == tar):
            return mid
        elif(arr[mid] > tar):
            end = mid - 1
        else:
            ind = mid + 1

    return "false"

starttime = time.time()
print(findInArr(5, numbers))
print(time.time() - starttime)
# 0.000 sec vs 0.003 on linearsearch