def find_mean(arr):
    total = 0
    for i in range(len(arr)):
        total += arr[i]
    mean = total // len(arr)
    return mean

arr = [13, 20, 33, 43, 50]
print(find_mean(arr))