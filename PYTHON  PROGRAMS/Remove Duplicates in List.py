list1 = [10, 20, 20, 30, 40, 10, 50, 20, 30, 50, 40, 60]
empty_list = []

for i in list1:
    if i not in empty_list:
        empty_list.append(i)
   
print(empty_list)