def removeDuplicate(arr):
    seen = set()
    result = []
    for i in arr:
        if i not in seen:
            seen.add(i)
            result.append(i)
    return result

arr = [1, 5, 2, 4, 2, 5, 6, 3, 7, 8, 3, 1, 6, 3]
print(removeDuplicate(arr))