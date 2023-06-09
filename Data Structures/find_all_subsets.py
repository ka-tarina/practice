# Find all subsets of given set


def find_all_subsets(my_set):
    sub_sets = [[]]
    final = []
    for i in my_set:
        for j in range(len(sub_sets)):
            sub_set = sub_sets[j]
            sub_sets.append(sub_set + [i])
    for j in sub_sets:
        final.append(set(j))
    return final


def sorting(my_list):
    s_set = sorted(my_list, key=len)
    return s_set


set_1 = {1, 2, 3}

print(sorting(find_all_subsets(set_1)))
