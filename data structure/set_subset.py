
first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}
print("First set is:",first_set)
print("Second set is:",second_set)
sub = first_set.issubset(second_set)
sub1 = second_set.issubset(first_set)
print("First set is subset of second set:",sub)
print("Second set is subset of first set:",sub1)
super = first_set.issuperset(second_set)
super1 = second_set.issuperset(first_set)
print("First set is superset of second set:",super)
print("Second set is superset of first set:",super1)
if first_set.issubset(second_set):
    print(first_set.clear())
if second_set.issubset(first_set):
    print(second_set.clear())
