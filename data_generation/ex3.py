# Exercise 3: Generate 6 digit random secure OTP
import random
def otp():
    for i in range(1):
        return random.randrange(100000,999999)
print("Yout OTP is : ",otp())