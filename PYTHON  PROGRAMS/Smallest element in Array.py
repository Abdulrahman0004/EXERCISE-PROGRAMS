arr = [10, 6, 4, 2, 7, 9, 2, 5]
small = arr[0]

for i in range(len(arr)):
    if arr[i] <= small:
        small = arr[i]
print(small)