#4. Write a Python program to find a factorial of a given number

num = int(input("Enter the number: "))
fact = 1
for i in range(num, 0, -1):
    fact = fact * i
print("The Factorial of", num, "is", fact)