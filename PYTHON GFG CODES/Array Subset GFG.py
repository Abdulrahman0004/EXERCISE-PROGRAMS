from collections import Counter 

def Subset(a, b):
    count_a = Counter(a)
    count_b = Counter(b)

    for i in count_b:
        if count_b[i] > count_a[i]:
            return False
    return True

a = [1, 1, 2, 2, 2, 3, 4, 4, 5]
b = [1, 1, 2, 2, 3, 4]
print(Subset(a, b))