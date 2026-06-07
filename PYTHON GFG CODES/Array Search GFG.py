def Search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
        
arr = [1, 2, 3, 4, 5]
x = 6
print(Search(arr, x))