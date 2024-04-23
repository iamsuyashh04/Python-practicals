#  1 Write a Python program to demonstrate any 10 methods of List.

# Creating a list
my_list = [1, 2, 3, 4, 5]

# 1. append() - Adds an element to the end of the list
my_list.append(6)
print("1. Append:", my_list)

# 2. extend() - Appends elements from another list to the current list
other_list = [7, 8, 9]
my_list.extend(other_list)
print("2. Extend:", my_list)

# 3. insert() - Inserts an element at a specified index
my_list.insert(2, 10)
print("3. Insert:", my_list)

# 4. remove() - Removes the first occurrence of a value
my_list.remove(3)
print("4. Remove:", my_list)

# 5. pop() - Removes and returns the element at the specified index (default is the last element)
popped_element = my_list.pop(4)
print("5. Pop (Removed element):", popped_element)
print("   List after pop:", my_list)

# 6. index() - Returns the index of the first occurrence of a value
index_of_4 = my_list.index(4)
print("6. Index of 4:", index_of_4)

# 7. count() - Returns the number of occurrences of a value
count_of_5 = my_list.count(5)
print("7. Count of 5:", count_of_5)

# 8. reverse() - Reverses the order of elements in the list
my_list.reverse()
print("8. Reverse:", my_list)

# 9. sort() - Sorts the list in ascending order (for numbers) or alphabetical order (for strings)
my_list.sort()
print("9. Sort (Ascending):", my_list)

# 10. clear() - Removes all elements from the list
my_list.clear()
print("10. Clear:", my_list)
