def repeatingArray(arr):
    if len(arr) == 0:
        return None
    result = {}

    for i in range(len(arr)):
        if arr[i] not in result:
            result[arr[i]] = 1
        else:
            result[arr[i]] += 1

    for key in result:
        if result[key] == 1:
            print(key)

arr = [1, 2, 3, 2, 3, 4, 5, 6, 7]
repeatingArray(arr)