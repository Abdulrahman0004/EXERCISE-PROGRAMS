arr = [1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5]
k = 3

result = -1
first = 0
last = len(arr)-1

while first <= last:
    mid = (first + last) // 2
    if arr[mid] == k:
        result = mid
        last = mid - 1
    elif arr[mid] < k:
        first = mid + 1
    elif arr[mid] > k:
        last = mid - 1
print(result)

