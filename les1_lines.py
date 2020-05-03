#!/usr/bin/env python3
import random

#### 1
print(" ")
print("1st task")
print("###Given lines:")
line1 = "He became the first human to journey into outer space on 12 April 1961."
line2 = "He was the first person to walk on the Moon on July 20, 1969."
print(line1)
print(line2)

def del_fist_letter(str):
    arr_line = list(str)
    new_line = ''.join(arr_line[1:])
    return new_line

print("###RESULT. Lines concatination:")
print(del_fist_letter(line1)+del_fist_letter(line2))
print(" ")


#### 2
print("2nd task")
print("###Given line:")
line3="The only source of knowledge is the experience."
print(line3)

arr_line3 = list(line3)
new_line3 = ''.join(arr_line3[-3:-1])

print("###RESULT:")
print(new_line3*3)
print(" ")

#### 3
print("3d task")
print("###Given list:")
list1 = (111, 333, 444, 222)
print(list1)
list_sorted1 = sorted(list1)
new_list1 = []
counter = 0
element = int(-1)

while counter < len(list1):
    new_list1.append(list_sorted1[element])
    element = element - 1
    counter = counter + 1

print("###RESULT:")
print(new_list1)
print(" ")

#### 4
print("4th task")
print("###Given list:")
list2 = (555, 333, 101, 222)
print(list2)

sorted_list2 = sorted(list2)
counter = 0
new_list2 = []

while counter < len(list2):
    new_list2.append(sorted_list2[-1])
    counter = counter + 1

print("###RESULT:")
print(new_list2)
print(" ")

#### 5
print("5th task")
print("###Given list:")
list3 = random.sample(range(1, 100), 20)
print(list3)

digit = 0
sum = 0

for digit in list3:
    if 13 <= digit <= 14 or 17 <= digit <= 19:
        pass
    elif digit == 15:
        sum = sum + digit
    elif digit == 16:
        sum = sum + digit
    else:
        sum = sum + digit

print("###RESULT:")
print(sum)




