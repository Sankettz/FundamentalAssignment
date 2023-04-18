my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3)
repeated_items = set(item for item in my_tuple if my_tuple.count(item) > 1)
print(repeated_items)