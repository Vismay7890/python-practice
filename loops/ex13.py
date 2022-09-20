# Exercise 14: Reverse a given integer number
n = 76542
rev = 0
while n > 0:
    rem = n % 10
    rev = (rev * 10) + rem
    n = n // 10
print(rev)