def search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# Example usage:
arr = [1, 2, 3, 4, 5]
x = 10
result = search(arr, x)
print(result)