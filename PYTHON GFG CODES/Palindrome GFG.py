def Palindrome(arr):
    if arr != arr[::-1]:
         return False
    return True

arr = [1, 2, 3, 2, 1]
print(Palindrome(arr))