arr = [2, 5, 7, 10, 6, 3, 2, 11, 9, 8, 12]
large = float('-inf')
second_large = float('inf')

for i in range(len(arr)):
    if arr[i] > large:
        second_large = large
        large = arr[i]
    elif arr[i] > second_large and arr[i] != large:
        second_large = arr[i]

print(second_large)