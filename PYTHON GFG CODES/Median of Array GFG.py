def find_Median(arr):
    if len(arr) == 0:
        return None
    arr.sort()
    if len(arr) % 2 == 1:
        mid = len(arr) // 2
        return arr[mid]
    else:
        mid = len(arr) // 2
        avg = (arr[mid] + arr[mid-1]) / 2
        return avg
    
arr = [13, 20, 43, 50]
print(find_Median(arr))