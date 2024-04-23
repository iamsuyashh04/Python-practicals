# Write a Python program to demonstrate any 10 methods of Dictionary.

# Creating a dictionary
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "email": "john@example.com"
}

# 1. get() - Returns the value for the specified key
print("1. Get:")
name = my_dict.get("name")
print("Name:", name)

# 2. keys() - Returns a list of all the keys
print("\n2. Keys:")
keys = my_dict.keys()
print("Keys:", keys)

# 3. values() - Returns a list of all the values
print("\n3. Values:")
values = my_dict.values()
print("Values:", values)

# 4. items() - Returns a list of key-value pairs (tuples)
print("\n4. Items:")
items = my_dict.items()
print("Items:", items)

# 5. pop() - Removes the item with the specified key
print("\n5. Pop:")
removed_item = my_dict.pop("age")
print("Removed Item:", removed_item)
print("Dictionary after pop:", my_dict)

# 6. popitem() - Removes the last inserted key-value pair
print("\n6. Popitem:")
last_item = my_dict.popitem()
print("Last Item:", last_item)
print("Dictionary after popitem:", my_dict)

# 7. update() - Updates the dictionary with the specified key-value pairs
print("\n7. Update:")
my_dict.update({"city": "Los Angeles", "phone": "123-456-7890"})
print("Updated Dictionary:", my_dict)

# 8. clear() - Removes all items from the dictionary
print("\n8. Clear:")
my_dict.clear()
print("Cleared Dictionary:", my_dict)

# Re-populating the dictionary
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "email": "john@example.com"
}

# 9. copy() - Returns a copy of the dictionary
print("\n9. Copy:")
copied_dict = my_dict.copy()
print("Copied Dictionary:", copied_dict)

# 10. setdefault() - Returns the value of the specified key, if present. If not, inserts the key with the specified value.
print("\n10. Setdefault:")
value = my_dict.setdefault("city", "Unknown")
print("Value for 'city':", value)
value = my_dict.setdefault("gender", "Male")
print("Value for 'gender':", value)
print("Dictionary after setdefault:", my_dict)
