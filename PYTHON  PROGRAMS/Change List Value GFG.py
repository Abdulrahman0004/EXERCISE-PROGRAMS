list1 = [10, 20, 30, 40, 50]
list1[2] = 35
list1[4] = 55
list1[0] = 15

print(list1)


# Change elements using slicing
list1[1:4] = [29, 39, 49]
print(list1)


#Change elements using loop and enumerate()
for i, j in enumerate(list1):
    if j % 2 == 0:
        list1[i] = j + 5
    print(list1[i], end=' ')
print()

for i, j in enumerate(list1):
    if j % 2 != 0:
        list1[i] = j - 5
    print(list1[i], end=' ')