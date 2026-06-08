arr = [9, 8, 7, 6, 4, 2, 1, 3]

def RotateArray(arr):
    temp = arr[len(arr)-1]
    for i in range(len(arr)-1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = temp
    return arr

print(RotateArray(arr))