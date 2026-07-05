def sumArray(arr):
    total = 0
    for i in range(len(arr)):
        total = arr[i] + total
    return total

arr = [15, 32, 35, 30, 55]
print(sumArray(arr))