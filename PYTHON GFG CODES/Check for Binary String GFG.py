str = '0101001'
i = 0

while i < len(str)-1:
    if str[i] == '0' or str[i] == '1':
        i += 1
        continue
    else:
        print('False')
        break
else:
    print("True")
