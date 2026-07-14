from collections import Counter
str1 = 'hello'
str2 = 'lelol'

count_str1 = Counter(str1)
count_str2 = Counter(str2)

if count_str1 == count_str2:
    print("It is Anagram")
else:
    print("It is not Anagram")



