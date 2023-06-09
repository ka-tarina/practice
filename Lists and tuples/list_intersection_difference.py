# Make functions that take 2 lists as arguments and return their intersection/difference.


def intersection(list_1, list_2):
    list_3 = []
    for i in list_1:
        if i in list_2:
            list_3.append(i)
    return list_3


def difference(list_1, list_2):
    list_3 = []
    for i in list_1:
        if i not in list_2:
            list_3.append(i)
    for j in list_2:
        if j not in list_1:
            list_3.append(j)
    return list_3


lista1 = [10, 20, 30, 40]
lista2 = [10, 30, 50, 70]

print(intersection(lista1, lista2))
print(difference(lista1, lista2))
