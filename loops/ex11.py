# Exercise 12: Display Fibonacci series up to 10 terms
num1 = 0 
num2 = 1
for i in range(10):
    print(num1)
    res = num1+num2
    num1 = num2
    num2 = res