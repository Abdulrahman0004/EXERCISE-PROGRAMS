s1 = "abcdefg"
num = ""
numbers = []

for i in s1:
    if i.isdigit():
        num += i
    elif num:
        numbers.append(int(num))
        num = ""

if num:
    numbers.append(int(num))

if numbers == []:
    print(-1)
else:
    print(max(numbers))