list1 = [1, 2, 3, 1, 6, 7, 90, 4, 5]
list2 = [5, 6, 7, 5, 70, 90, 75, 4, 1]
list3 = []

# 1st task
print(len(set(list1)))

# 2nd and 3d task
list1s = set(list1)
list2s = set(list2)

count = 0
while count < len(list2s):
    for i in list2s:
        if i in list1s:
            list3.append(i)
        count += 1
print(f"list3 = {list3}")

# 4th task
line1 = '1 2 67 8 9 0 3 2 67 87 65 69 5 2'
#line2 = (list(line1.split(' ')))

#list4 = []
#for i in line2:
#    list4.append(int(i))

line2 = [int(x) for x in line1.split(’ ’)]


list5 = []
for e in list4:
    if e in list5:
        print('YES')
        list5.append(e)
    else:
        print('NO')
        list5.append(e)

list5 = list(set(line2))