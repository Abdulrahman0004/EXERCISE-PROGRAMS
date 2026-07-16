arr = [-1, 2, -3, 4, -5, 6]
positive = []
negative = []
result = []

for i in range(len(arr)):
    if arr[i] < 0:
        negative.append(arr[i])
    else:
        positive.append(arr[i])

for i in range(len(positive)):
    result.append(positive[i])
    result.append(negative[i])

print(result)
