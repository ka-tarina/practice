"""
Make a sum of elements of 2 tuples so that the elements of the first are added to
to elements with the same index from the second tuple.
"""

t1 = (1, 2, 3)
t2 = (3, 3, 5)
final = []
i = 0

while i != len(t1):
    suma = t1[i] + t2[i]
    final.append(suma)
    i += 1

t3 = tuple(final)
print(t3)
