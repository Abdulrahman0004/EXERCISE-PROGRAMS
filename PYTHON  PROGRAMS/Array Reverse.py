# Method 1 Using Function and loop
def reverseArray(a):
    n = len(a)
    first = 0
    last = n-1
    while first < last:
        a[first], a[last] = a[last], a[first]
        first = first + 1
        last = last - 1
    return a

a = [1, 2, 3, 4, 5]
print(reverseArray(a))



# Method 2 using Slicing
list1 = [1, 2, 3, 4, 5]
print(list1[::-1])



# Method 3 using reverse() function
list1 = [10, 20, 30, 40, 50]
list1.reverse()
print(list1)



# Method 4 using reversed() function
print(list(reversed(list1)))