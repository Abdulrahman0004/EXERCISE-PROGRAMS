arr = [1, 2, 3, 1, 2, 5, 6, 3, 1, 7]
frequency = {}

for i in range(len(arr)):
    if arr[i] not in frequency:
        frequency[arr[i]] = 1
    else:
        frequency[arr[i]] += 1

for key in frequency:
    print(key, frequency[key])

