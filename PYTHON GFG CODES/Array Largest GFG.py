def largest(arr):
        if len(arr) == 0:
            return None
        max = arr[0]
        for i in range(1, len(arr)):
            if arr[i] > max:
                max = arr[i]
        return max

arr = [9, 8, 7, 6, 4, 20, 1, 3]
print(largest(arr))