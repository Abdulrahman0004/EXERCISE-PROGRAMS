num = 9878

while num >= 10:
    total = 0
    while num > 0:
        digit = num % 10
        total = digit + total
        num = num // 10
    num = total
print(num)