n = 5
arr = [2, 3, 5, 7]
s_arr = set(arr)
count = 0

for i in s_arr:
    if (i-1 in arr) and (i+1 in arr):
        count += 1

print(count)
