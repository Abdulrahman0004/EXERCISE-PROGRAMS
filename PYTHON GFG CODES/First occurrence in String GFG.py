str1 = "GeeksForGeeks"
pat = "gr"

left = 0
right = len(pat)

for i in range(left, len(str1) - len(pat)+1):
    if str1[left:right] == pat:
        print(left)
        break
    else:
        left += 1
        right += 1
else:
    print(-1)