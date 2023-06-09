# Add element X before every element in given list:

def insert_x(some_list, x):
    for i in range(0, len(some_list)*2, 2):
        some_list.insert(i, x)
    return some_list


list_1 = [2, 4, 6, "k", 8]

print(insert_x(list_1, "x"))
