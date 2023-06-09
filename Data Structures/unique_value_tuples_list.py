# Find unique values in a list of tuples.


def get_unique_values(my_list):
    the_list = []
    for i in my_list:
        for j in i:
            if j in the_list:
                continue
            else:
                the_list.append(j)
    return the_list


lista = [("h", "g", "l", "k"), ("a", "b", "d", "e", "c"), ("j", "i", "y"), ("n", "b", "v", "c"), ("x", "z")]

print(get_unique_values(lista))
