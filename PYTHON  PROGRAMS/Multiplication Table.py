#3. Write a Python program to print multiplication table for a given number

num = int(input("Multiplication Table for :"))
for i in range(1, 11):
    print(num, "*", i, " = ", num*i)