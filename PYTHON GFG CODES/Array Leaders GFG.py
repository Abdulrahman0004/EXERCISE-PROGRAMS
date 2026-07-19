arr = [16, 17, 4, 3, 5, 2]
emp_arr = []
leader = arr[len(arr)-1]

for i in range(len(arr)-1, -1, -1):
    if leader <= arr[i]:
        emp_arr.append(arr[i])
        leader = arr[i]

emp_arr.reverse()
print(emp_arr)