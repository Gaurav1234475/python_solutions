def unique(list):
    unique_list = []
    for x in list:
        if x not in unique_list:
            unique_list.append(x)

    for x in unique_list:
        print (x)
list = [10, 20, 10, 30, 40, 50, 40, 30]
print("the unique value from list are")
unique(list)