first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}
print("First set is :" , first_set)
print("second set is :" , second_set)
intersection = first_set.intersection(second_set)
print("intersection is :",intersection)
for item in intersection:
    first_set.remove(item)
print("First Set after removing common element ", first_set)
