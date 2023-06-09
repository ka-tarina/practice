# Check if all elements in a list are the same type.


def element_type_same(my_list):
    x = my_list[0]
    counter = 0
    for i in my_list:
        if type(x) == type(i):
            counter += 1
    if counter == len(my_list):
        return True
    else:
        return False


lista_1 = [1, 2, 3, 4, 5]
lista_2 = [1, "a", 2, 3, "b"]

print(element_type_same(lista_1))
print(element_type_same(lista_2))
