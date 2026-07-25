arr = [2, 4, 7, 1, 3, 6]
target = 9
seen = {}
result = []


for i in range(len(arr)):
    need = target - arr[i]
    if need in seen:
        result.append((need, arr[i]))
    seen[arr[i]] = 1
print(result)
