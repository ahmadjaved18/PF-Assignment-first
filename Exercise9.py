list1 = [1,3,5,7,8,9,12,15,18]
list2 = [2,4,6,8,10,13,16,17]
new_list = []
for num in list1:
    if num % 2 == 1:
        new_list.append(num)
for num in list2:
    if num % 2 == 0:
        new_list.append(num)
print("Our new list = ", new_list)
