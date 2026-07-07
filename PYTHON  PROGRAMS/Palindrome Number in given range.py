def isPalindrome(num):
    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10
    return original == reverse

def palindromeRange(start, end):
    for i in range(start, end + 1):
        if isPalindrome(i):
            print(i)

start = 10
end = 50
palindromeRange(start, end)