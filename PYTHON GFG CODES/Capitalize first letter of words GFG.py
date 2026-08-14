s = "i love programming"
result = ""

for i in range(len(s)):
    if i == 0:
        result += s[i].upper()

    elif s[i] == " ":
        result += s[i]

    elif s[i-1] == " ":
        result += s[i].upper()

    else:
        result += s[i]

print(result)