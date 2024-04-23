# Write a Python program to demonstrate working on tuples and any methods of Tuple.

# Creating a tuple
my_tuple = (1, 2, 3, 4, 2, 5)

# Accessing elements of a tuple
print("1. Accessing elements:")
print("First element:", my_tuple[0])
print("Third element:", my_tuple[2])
print("Last element:", my_tuple[-1])
print("")

# 2. index() - Returns the index of the first occurrence of a value
index_of_2 = my_tuple.index(2)
print("2. Index of 2:", index_of_2)

# 3. count() - Returns the number of occurrences of a value
count_of_2 = my_tuple.count(2)
print("3. Count of 2:", count_of_2)
print("")

# Unpacking a tuple
a, b, c, d, e, f = my_tuple
print("4. Unpacking tuple:")
print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)
print("e:", e)
print("f:", f)
print("")

# Combining tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print("5. Combining tuples:")
print("Combined Tuple:", combined_tuple)
print("")

# Converting tuple to list
tuple_to_list = list(my_tuple)
print("6. Converting tuple to list:")
print("Tuple to List:", tuple_to_list)
print("")

# Slicing a tuple
sliced_tuple = my_tuple[1:4]
print("7. Slicing tuple:")
print("Sliced Tuple:", sliced_tuple)
print("")

# Checking membership in tuple
print("8. Checking membership:")
print("Is 3 in tuple?", 3 in my_tuple)
print("Is 10 in tuple?", 10 in my_tuple)
print("")

# Length of tuple
print("9. Length of tuple:")
print("Length of my_tuple:", len(my_tuple))
print("")

# Min and Max in tuple
print("10. Min and Max in tuple:")
print("Min of my_tuple:", min(my_tuple))
print("Max of my_tuple:", max(my_tuple))
print("")

# Tuple packing
packed_tuple = 1, 2, 3
print("11. Tuple packing:", packed_tuple)

# Tuple unpacking
x, y, z = packed_tuple
print("12. Tuple unpacking:")
print("x:", x)
print("y:", y)
print("z:", z)
