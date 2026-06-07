arr = [25, 35, 60, 50, 20, 10, 5, 30]

def MinMax(arr):
    min = arr[0]
    max = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min:
            min = arr[i]
        elif arr[i] > max:
            max = arr[i]
    return [min, max]

print(MinMax(arr))