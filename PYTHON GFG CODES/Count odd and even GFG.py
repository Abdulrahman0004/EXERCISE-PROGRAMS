arr = [1, 1]
odd_count = 0
even_count = 0

for i in range(len(arr)):
    if arr[i] % 2 == 1:
        odd_count += 1
    else:
        even_count += 1

print(odd_count, even_count)