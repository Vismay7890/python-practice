l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
l3_odd = []
l4_even = []
for i in range(len(l1)):
    if i%2!=0:
        l3_odd.append(l1[i])
for j in range(len(l2)):
    if j%2==0:
        l4_even.append(l2[j])
print(l3_odd)
print(l4_even)
print(l3_odd+l4_even)