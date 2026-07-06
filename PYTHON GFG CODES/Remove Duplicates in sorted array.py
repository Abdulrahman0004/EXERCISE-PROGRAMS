def removeDuplicates(arr):
    first = 0
    if len(arr) == 0:
        return None
    for i in range(1, len(arr)):
        if arr[i] != arr[first]:
            first += 1
            arr[first] = arr[i]
    return arr[:first+1]

arr = [10, 10, 20, 20, 20, 30, 40, 40, 50, 50, 50]
print(removeDuplicates(arr))