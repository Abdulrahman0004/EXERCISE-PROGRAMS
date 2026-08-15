n = 1222334455678900
num = str(n)
result = num[0]

for i in range(1, len(num)):
    if num[i] != num[i-1]:
        result += num[i]

print(result)