text = input()
text = text.replace(" ", "").lower()
low = 0
high = len(text)-1

while low <= high:
    if text[low] != text[high]:
        print("It is not a Palindrome")
        break
    else:
        low += 1
        high -= 1
else:
    print("It is a Palindrome")
