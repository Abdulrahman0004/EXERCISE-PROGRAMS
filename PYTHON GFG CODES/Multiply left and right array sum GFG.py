arr = [1, 2]
mid = len(arr) // 2
sum1 = 0
sum2 = 0

for i in range(mid):
    sum1 += arr[i]

for i in range(mid, len(arr)):
    sum2 += arr[i]

product = sum1 * sum2
print(product)
