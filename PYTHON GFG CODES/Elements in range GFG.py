def checkRange(arr, start, end):
    for i in range(start, end+1):
        if i not in arr:
            return False
    return True

arr = [1, 4, 5, 2, 7, 8, 3]
print(checkRange(arr, 1, 5))