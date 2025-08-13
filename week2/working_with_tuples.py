### Tuples
# A tuple is an ordered, immutable (unchangeable) collection of items in Python.

# Creating Tuples
# 1. Using parentheses ()
# Example 1: tuple with multiple items
fruits = ("apple", "banana", "cherry")
fruit = ["apple", "banana", "cherry"]
print(fruits)           # ('apple', 'banana', 'cherry')
print("fruits type", type(fruits))
print("fruit type", type(fruit))

# 2. Without parentheses (tuple packing)
numbers = 1, 2, 3
print(numbers)          # (1, 2, 3)
print(type(numbers))

# 3. Single-item tuple (must include a comma)
single_item = ('apple',)
print(single_item)          # ('apple',)
print(type(single_item))

# 4. Using the tuple() constructor
fruits_list = ["apple", "banana","cherry"]
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)

# Characteristics of Tuples
#1. Ordered - items have a fixed position.
#2. Immutable - cannot change after creation.
#3. Allow duplicates - same value can appear multiple times.
#4. Can contain mixed data types - strings, integers, lists etc.
#5. Can be nested - tuples inside tuples.
# Ordered
colors = ("red", "green", "blue")
print(colors[0])        # red

# Immutable (uncomment and run. this will cause an error)
#colors[1] = "yellow"    # TypeError

# Allow duplicates
numbers = (1, 2, 2, 3)
print(numbers)          # Output: (1, 2, 2, 3)

# Mixed data types
mixed = ("apple", 3, True, 5.6)
print(mixed)            # ('apple', 3, True, 5.6)
print(type(mixed))

# Nested tuples
nested = (("a", "b"), (1, 2))
print(nested)           # (('a', 'b'), (1, 2))

# Tuple Operations
# Even though tuples are immutable, you can still perform several operations
#1. Indexing
fruits = ("apple", "banana", "cherry")
print(fruits[1])        # banana
print(fruits[-1])       # cherry

#2. Slicing
print(fruits[0:2])      # ('apple', 'banana')
print(fruits[::-1])     # ('cherry', 'banana', 'apple')

#3. Concatenation
tuple1 = (1, 2)
tuple2 = (3, 4)
result = tuple1 + tuple2
print(result)           # (1, 2, 3, 4)

#4. Repetition
nums = (1, 2)
print(nums * 3)         # (1, 2, 1, 2, 1, 2)

#5. Membership
fruits = ("apple", "banana", "cherry")
print("banana" in fruits)       # True
print("grape" not in fruits)    # True

#6. Iteration
for fruit in fruits:
    print(fruit)


# Working with Tuples
# You can't modify a tuple directly, but you can;
#    convert it to a list, modify it, then convert back.
#    use built-in functions to work with tuple contents.

### 1. Unpacking Tuples
person = ("John", 25, "Nigeria")
name, age, country = person 
print(name)        # John
print(age)         # 25
print(country)     # Nigeria


# Tuple methods
# Tuples have only two methods
# dot count() and dot index()
numbers = (1, 2, 2, 3, 4)
print(numbers.count(2))     # 2 (count occurences of 2)
print(numbers.index(3))     # 3 (position of first occurence of 3)


# Converting Between List and Tuple
# Tuple to List
t = (1, 2, 3)
lst = list(t)
lst.append(4)
print(lst)              # Output: [1, 2, 3, 4]
print(tuple(lst))       # Output: (1, 2, 3, 4)

# Built-in Functions with Tuples
nums = (4, 1, 7, 3)
print(len(nums))        # 4
print(max(nums))        # 7
print(min(nums))        # 1
print(sum(nums))        # 15
