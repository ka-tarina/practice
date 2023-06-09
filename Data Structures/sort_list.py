# Sort list - ascending.

def sort_list(some_list):
    for i in range(len(some_list)):
        for j in range(len(some_list) - 1):
            if some_list[j] > some_list[j + 1]:
                some_list[j], some_list[j + 1] = some_list[j + 1], some_list[j]
    return some_list


list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 4, 5, 3, 4, 2, 0, 5]

print(sort_list(list_1))
