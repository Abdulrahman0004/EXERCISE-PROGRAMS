n = int(input())
if n % 2 == 1:
    print('Weird')
if n in range(2, 5) and n % 2 == 0:
    print('Not Weird')
if n in range(6, 21) and n % 2 == 0:
    print("Weird")
if n % 2 == 0 and n > 20:
    print("Not Weird")
