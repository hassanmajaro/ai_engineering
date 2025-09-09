###List Methods
# Python provides many built-in methods for working with lists. Here is each method, what it does, and an example.
#1. dot append() method
# adds an element to the end of the list.
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)           # Output: ['apple', 'banana', 'cherry']

#2. dot insert() method
# inserts an element at a specific position
fruits = ["apple", "banana"]
fruits.insert(1, "orange")
print(fruits)           # Output: ['apple', 'orange', 'banana']

#3. dot extend() method
# adds elements from another list (or iterable) to the end.
fruits = ["apple", "banana"]
tropical = ["mango", "pineapple"]
fruits.extend(tropical)
print(fruits)           # Output: ['apple', 'banana', 'mango', 'pineapple']

#4. dot remove() method
# removes the first occurent of a specified value
fruits = ["apple", "banana", "cherry", "banana"]
fruits.remove("banana")
print(fruits)           # Output: ['apple', 'cherry', 'banana']

#5. dot pop() method
# removes and returns the element at a given index (default: last).
fruits = ["apple", "banana", "cherry"]
last_fruit = fruits.pop()       # Output: cherry
print(last_fruit)
print(fruits)                   # Output: ['apple', 'banana']

#6. dot clear() method
# removes all elements from the list.
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)                   # Output: []

#7. dot index() method
fruits = ["apple", "banana", "cherry"]
position = fruits.index("banana")
print(position)                 # Output: 1

#8. dot count() method
# counts how many times a value appears.
fruits = ["apple", "banana", "cherry", "banana"]
print(fruits.count("banana"))   # Output: 2

#9. dot sort() method
# sorts the list in ascending order (default).
numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)          # Output: [1, 2, 3, 4]

# descending order
numbers.sort(reverse=True)
print(numbers)          # Output: [4, 3, 2, 1]

#10. dot reverse() method
# reverses the order of the list
fruits = ["apple", "banana", "cherry"]
fruits.reverse()
print(fruits)           # Output: ['cherry', 'banana', 'apple']

#11. copy()
# returns a shallow copy of the list 
fruits = ["apple", "banana", "cherry"]
new_list = fruits.copy()
print(new_list)         # Output: ['apple', 'banana', 'cherry']