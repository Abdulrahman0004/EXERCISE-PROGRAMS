#4. Write a Python Program to display only those numbers from a list that satisfy the following conditions
# The Number must be divisible by 5
# If the number is greater than 150, then skip it and move on to the next number
# If the number is greater than 500, then stop the loop

numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
        if i > 500:
            break
        elif i > 150:
            continue
        elif i % 5 == 0:
            print(i)