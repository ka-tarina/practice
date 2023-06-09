# Find then print max element in a list.


some_list = [4, 65, 46, 1, 6, 0, 48, 64, 15, 2, 0, 8, 74, 8]
max_el = 0

for num in some_list:
    if num > max_el:
        max_el = num

print(max_el)
