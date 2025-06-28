def BinarySearch(list1, key):
    low = 0
    high = len(list1)-1
    while low <= high:
        mid = (low+high) // 2
        if list1[mid] == key:
            print("Key is found at index:", mid)
            return
        elif list1[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    print("Key is not found...")
list1 = [1, 5, 2, 7, 8, 4, 20, 15, 33, 46, 17, 23, 12, 3, 9, 40, 30]
list1.sort()
print(list1)
key = int(input("Enter the key: "))
BinarySearch(list1, key)
