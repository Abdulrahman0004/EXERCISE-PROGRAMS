arr = [299, 5, 1, 30]
large = arr[0]

for i in range(len(arr)):
    if arr[i] >= large:
        large = arr[i]
print(large)