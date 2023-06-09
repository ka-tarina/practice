# Make a function that generates sub-lists from given list.


def sub_lists(my_list):
    final_lists = [[]]
    for i in my_list:
        for j in range(len(final_lists)):
            temp_list = final_lists[j].copy()
            temp_list.append(i)
            final_lists.append(temp_list)
    return final_lists


def sorting(my_list):
    s_list = sorted(my_list, key=len)
    return s_list


list_1 = [10, 20, 30, 40]
print(sorting(sub_lists(list_1)))
