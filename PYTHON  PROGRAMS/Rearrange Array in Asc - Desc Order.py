def asc_descSort(arr):
    asc_arr = sorted(arr)
    desc_arr = sorted(arr, reverse=True)
    result = []

    mid = len(arr) // 2
    for i in range(mid):
        result.append(asc_arr[i])
    for i in range(mid):
        result.append(desc_arr[i])
    return result

arr = [1, 5, 2, 6, 8, 9, 3, 5]
print(asc_descSort(arr))