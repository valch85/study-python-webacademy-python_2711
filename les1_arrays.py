#!/usr/bin/env python3

array = [1, 2, 3333, 40, 5, 6, -1, 0, -1, 3333, 5]

# sum of even digits
sum = 0
for element in array:
    if element % 2 == 0:
        sum += element
print(sum)

# sum max and min elements
print(min(array)+max(array))

# upgoing array
print(sorted(array))

# downgoing array
print(sorted(array, reverse=True))

# unique
print ("unique: ")
print (len(set(array)))

# amount of non-unique
answer = []
for element in array:
    if array.count(element) > 1:
        answer.append(element)

answer = ', '.join(str(e) for e in set(answer))

if not answer:
    print("List is empty")
else:
    print(f"Array has non-unique elements {answer}")

# delete last and first elements
array_new = array[1:-1]
print(array_new)

# reverse sort
print(sorted(array, reverse=True))