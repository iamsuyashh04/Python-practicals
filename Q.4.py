# Write a Python program to demonstrate any 10 methods of Sets.

# Creating sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# 1. add() - Adds an element to the set
print("1. Add:")
set1.add(6)
print("After adding 6:", set1)

# 2. update() - Adds multiple elements to the set
print("\n2. Update:")
set1.update([7, 8, 9])
print("After updating with [7, 8, 9]:", set1)

# 3. remove() - Removes a specific element from the set, raises KeyError if element is not found
print("\n3. Remove:")
set1.remove(6)
print("After removing 6:", set1)

# 4. discard() - Removes a specific element from the set, does nothing if element is not found
print("\n4. Discard:")
set1.discard(9)
print("After discarding 9:", set1)

# 5. pop() - Removes and returns an arbitrary element from the set
print("\n5. Pop:")
popped_element = set1.pop()
print("Popped element:", popped_element)
print("Set after pop:", set1)

# 6. union() - Returns a new set with elements from both sets
print("\n6. Union:")
union_set = set1.union(set2)
print("Union of set1 and set2:", union_set)

# 7. intersection() - Returns a new set with elements common to both sets
print("\n7. Intersection:")
intersection_set = set1.intersection(set2)
print("Intersection of set1 and set2:", intersection_set)

# 8. difference() - Returns a new set with elements in set1 but not in set2
print("\n8. Difference:")
difference_set = set1.difference(set2)
print("Difference of set1 and set2:", difference_set)

# 9. symmetric_difference() - Returns a new set with elements in either set but not both
print("\n9. Symmetric Difference:")
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric Difference of set1 and set2:", symmetric_difference_set)

# 10. clear() - Removes all elements from the set
print("\n10. Clear:")
set1.clear()
print("Set1 after clear:", set1)
