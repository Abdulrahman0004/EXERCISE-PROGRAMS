s1 = "geeksforgequekste"
s2 = "geeksandquiz"
emp_dict = {}

for chr in s1:
    emp_dict[chr] = 1

for chr in s2:
    if chr not in emp_dict:
        emp_dict[chr] = 2
    elif emp_dict[chr] == 1:
        emp_dict[chr] = 3

result = ""

for chr in emp_dict:
    if emp_dict[chr] == 1 or emp_dict[chr] == 2:
        result += chr

result = "".join(sorted(result))
print(result)
