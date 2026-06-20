def MissingArray(arr):
    for i in range(1, len(arr)+2):
        if i in arr:
            continue
        return i
        
arr = [8, 2, 4, 5, 3, 7, 1]
print(MissingArray(arr))