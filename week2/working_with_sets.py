# ## Sets in Python
# # In Python, a set is an ordered collection of unique elements. Sets are useful when you want to store multiple items but aboid duplicates.
# # Creating Sets
# #1. Using curly braces
# fruits = {"apple", "banana", "mango"}
# print(fruits)

# #2. Using the set() constructor
# numbers = set([1, 2, 3, 4])
# print(numbers)

# #3. Creating an empty set (must use (), not {})
# empty_set = set()
# print(empty_set)

# #4. From a string (duplicates) removed automatically
# letters = set("mississippi")
# print(letters)

# # Characterisitics of Sets
# #1. Unordered: No defined indexing or sequence.
# #2. Unique elements: Duplicates are automatically removed.
# #3. Mutable: You can add or remove items.
# #4. Unindexed: You can't access elements using an index like my_set[0]
# #5. Supports mathematical set operations: Union, intersection, difference, symmetric difference.


# # Set Operations
# #a. Adding Elements
# colors = {"red", "blue"}
# colors.add("green")
# print(colors)

# #b. Removing Elements
# colors.remove("blue")       # Removes an element, raises error if not found
# #colors.remove("yellow")     # Removes if found, no error if missing
# print(colors)

# #c. Pop an element
# colors = {"red", "blue", "green"}
# removed = colors.pop()
# print("Removed:", removed)
# print("Remaining:", colors)

# #d. Clear a Set
# colors.clear()
# print(colors)


# #Mathematcial Set Operations
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}

# #1. Union
# print(set1 | set2)
# print(set1.union(set2))

# #2. Intersection
# print(set1 & set2)
# print(set1.intersection(set2))

# #3. Difference
# print(set1 - set2)
# print(set1.difference(set2))

# #4. Symmetric Difference
# print(set1 ^ set2)
# print(set1.symmetric_difference(set2))


# Working with Sets
# Collecting unique visitors to an event
visitors = set()

# Adding visitors
visitors.add("Chinedu")
visitors.add("Aisha")
visitors.add("Chinedu") # Duplicate, ignored automatically
print("Visitors:", visitors)

# #Checking if a visitor attended
# name = "Aisha"
# if name in visitors:
#     print(f"{name} attended the event.")
# else:
#     print(f"{name} did not attend the event.")