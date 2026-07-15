arr1 = [5, 4, 13, 5, 1]
arr2 = [5, 3, 6, 5, 1]

min1 = float('inf')
min2 = float('inf')
second1 = float('inf')
second2 = float('inf')

idx1 = -1
idx2 = -1

for i in range(len(arr1)):
    if arr1[i] < min1:
        second1 = min1
        min1 = arr1[i]
        idx1 = i
    elif arr1[i] < second1:
        second1 = arr1[i]

for i in range(len(arr2)):
    if arr2[i] < min2:
        second2 = min2
        min2 = arr2[i]
        idx2 = i
    elif arr2[i] < second2:
        second2 = arr2[i]

if idx1 != idx2:
    print(min1 + min2)
else:
    print(min(min1 + second2, second1 + min2))