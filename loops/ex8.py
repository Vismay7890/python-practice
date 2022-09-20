# Exercise 8: Print list in reverse order using a loop
list1 = [10, 20, 30, 40, 50]
for i in range(len(list1)):
    print(list1[-1])
    list1.pop(-1)
