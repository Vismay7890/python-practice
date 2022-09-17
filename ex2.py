l1 = [11, 45, 8, 23, 14, 12, 78, 45, 89]
length = len(l1)
chun = int(length/3)
start = 0
end = chun
for i in range(3):
    index = slice(start,end)
    list_chun = l1[index]
    print("chunk",i,list_chun)
    print("reversed list is :\n",list(reversed(list_chun)))
    start = end
    end += chun 