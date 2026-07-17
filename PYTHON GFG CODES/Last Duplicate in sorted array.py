def lastDuplicate(arr):
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == arr[i-1]:
            return [arr[i], i]
    return [-1, -1]


arr = [1, 2, 3, 4, 5]
print(lastDuplicate(arr))
