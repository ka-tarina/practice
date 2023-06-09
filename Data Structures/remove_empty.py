# Remove empty tuple from list.

list_1 = [(1, 2), (), ("A", "B"), ("X",), (), ()]

while () in list_1:
    list_1.remove(())

print(list_1)
