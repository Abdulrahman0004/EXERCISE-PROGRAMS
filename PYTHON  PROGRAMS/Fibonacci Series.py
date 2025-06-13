#7. Write a Python program to find the fibonacci series
num = int(input("Enter the no of terms in fibonacci series: "))
first = 0
second = 1
for i in range(num):
    print(first)
    temp = first
    first = second
    second = temp + first