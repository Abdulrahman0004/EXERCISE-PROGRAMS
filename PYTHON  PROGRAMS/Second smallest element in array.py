arr = [10, 5, 6, 4, 3, 1, 5, 6, 2]
small = float('inf')
second_small = float('inf')

for i in range(len(arr)):
    if arr[i] < small:
        second_small = small
        small = arr[i]
    elif arr[i] < second_small and arr[i] != small:
        second_small = arr[i]

if second_small == float('inf'):
    print(-1)
else:
    print(second_small)