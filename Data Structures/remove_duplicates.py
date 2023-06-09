# Remove duplicates from tuple.

def remove_duplicates(tup):
    final = []
    for i in tup:
        if i not in final:
            final.append(i)
    return final


exemp = (1, 1, 2, 2, 5, 5)

print(remove_duplicates(exemp))
