str1 = "aa"
str2 = "aa"

for i in str1:
    if i in str2:
        str1 = str1.replace(i, "")
        str2 = str2.replace(i, "")
str3 = str1 + str2

if str1 == str2:
    print(-1)
else:
    print(str3)