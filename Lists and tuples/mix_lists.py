"""
Mix elements from 2 lists so that the elements of the second are behind
elements of the first list. If one of the lists has more elements than
the other, add the remaining elements to the end of the resulting list.

"""


def mix_lists(list1, list2):
    mixed_list = []
    len_list1 = len(list1)
    for i in range(len_list1):
        mixed_list.append(list1[i])
        if i >= len(list2):
            continue
        mixed_list.append(list2[i])
    if len(list2) > len_list1:
        mixed_list.extend(list2[len_list1:])
    return mixed_list


l1 = ["A", "Xx"]
l2 = ["Y", 123, 9]

print(mix_lists(l1, l2))
