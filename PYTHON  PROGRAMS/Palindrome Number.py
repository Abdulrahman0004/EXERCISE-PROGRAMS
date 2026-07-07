def PalindromeNumber(num):
    rev = 0
    original = num 

    while num > 0:
        digit = num % 10
        rev = (rev*10) + digit
        num = num // 10
    return original == rev

num = 12325
print(PalindromeNumber(num))