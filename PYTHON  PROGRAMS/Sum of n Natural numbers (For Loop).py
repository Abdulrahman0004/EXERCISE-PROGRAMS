#2. Write a Python Program to calculate Sum of n Natural numbers using For Loop

num = int(input("Enter a number: "))
sum = 0
for i in range(1, num+1):
    sum = sum + i
print("The Sum is: ", sum)