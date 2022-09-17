l1 = [11, 45, 8, 11, 23, 45, 23, 45, 89]
print("List original:",l1)
count_dict = dict()
for item in l1:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1
print("Count for each item:",count_dict)