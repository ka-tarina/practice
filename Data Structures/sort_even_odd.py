# Create new list that takes the even numbers from one and odd numbers from another list and sort descending.


def even_odd(list_1, list_2):
    list_3 = []
    for i in list_1:
        if i % 2 == 0:
            list_3.append(i)
    for j in list_2:
        if j % 2 != 0:
            list_3.append(j)
    list_3.sort(reverse=True)
    return list_3


lista1 = [2, 1, 66, 4, 3, 87]
lista2 = [4, 4, 6, 99, 34, 3, 7, 10, -2, -10]

print(even_odd(lista1, lista2))
