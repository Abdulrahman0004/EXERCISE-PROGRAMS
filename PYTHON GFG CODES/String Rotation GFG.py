s1 = "hello"
s2 = "ohell"
 
if len(s1) != len(s2):
    print(False)
elif s2 in s1+s1:
    print(True)
else:
    print(False)

