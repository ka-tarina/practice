# Find and print unique values in a list.

def find_unique(some_list):
    new_list = []
    for elem in some_list:
        if some_list.count(elem) == 1:
            new_list.append(elem)
    return new_list


list_1 = [22, 18, 10, 1, 3, 7, 10, 3, 18]

print(find_unique(list_1))
