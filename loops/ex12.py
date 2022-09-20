# Write a program to use the loop to find the factorial of a given number.
n = int(input("Enter the number to find factorial:"))
fact = 1
if n == 0:
    print("Factorial of 0 is : 1")
elif n == 1:
    print("Factorial of 1 is : 1")
else:
    for i in range(1,n+1):
        fact = fact * i
    print(f"The factorial of {n} is:",fact)
