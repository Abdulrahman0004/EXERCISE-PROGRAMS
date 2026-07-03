str = "geeks..for.geekss"
words = []
current_str = ""

for i in str:
    if i != '.':
        current_str += i
    else:
        if current_str != "":
            words.append(current_str)
            current_str = ""
if current_str != "":
    words.append(current_str)

rev_list = words[::-1]

for i in range(len(rev_list)):
    if i == len(rev_list) - 1:
        print(rev_list[i], end="")
    else:
        print(rev_list[i], end=".")
