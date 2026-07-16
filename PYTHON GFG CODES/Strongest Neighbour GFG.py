arr = [5, 5]
emp_arr = []
first = 0

for i in range(1, len(arr)):
    if arr[first] <= arr[i]:
        emp_arr.append(arr[i])
        first += 1
    else:
        emp_arr.append(arr[first])
        first += 1
print(emp_arr)