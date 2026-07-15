num = int(input())
list1 = list(map(int, input().split()))
product = 1

for i in range(num):
    product *= list1[i] 
print(product)