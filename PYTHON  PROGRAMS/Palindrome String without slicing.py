str1 = 'malayalam'
low = 0
high = len(str1)-1

while low <= high:
    if str1[low] != str1[high]:
        print("It is not a Palindrome")
        break
    else:
        low += 1
        high -= 1
else:
    print("It is Palindrome")
    
