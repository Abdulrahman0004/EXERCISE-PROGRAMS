str = '01'
last = len(str)-1

for i in range(last, -1, -1):
    if str[i] == '1':
        print(i)
        break
else:
    print(-1)


