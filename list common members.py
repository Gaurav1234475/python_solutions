list1 = [1, 2, 3, 4, 5, 6]
list2 = [3, 5, 7, 9]
new_list = list(set(list1).intersection(list2))
print("common numbers are : " , new_list)