# 1. List
# Description: A list is an ordered, changeable collection of items.
# You can think of a list as a container where you can store different items
# in a specific order, and you can add, remove, or modify items as needed.
# Syntax: Use square brackets [] to define a list.
# Example:

fruits = ["apple", "banana", "cherry"]
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# Adding an item
fruits.append("orange")
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']

# Accessing an item
print(fruits[1])  # Output: 'banana'


# Real-World Analogy: A list is like a shopping list where each item has an order,
# and you can add or remove items whenever you want.
#
fruits.append("orange")
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']
# insert(): Adds an item at a specific position in the list.
fruits.insert(1, "kiwi")  # Adds "kiwi" at index 1
print(fruits)  # Output: ['apple', 'kiwi', 'banana', 'cherry', 'orange']

# extend(): Adds multiple items (from another list or any iterable) to the end of the list.
more_fruits = ["mango", "pineapple"]
fruits.extend(more_fruits)
print(fruits)  # Output: ['apple', 'kiwi', 'banana', 'cherry', 'orange', 'mango', 'pineapple']

# 3. Removing Items from a List
# remove(): Removes the first occurrence of a specified item.
fruits.remove("banana")
print(fruits)  # Output: ['apple', 'kiwi', 'cherry', 'orange', 'mango', 'pineapple']

# pop(): Removes the item at a specified index (or the last item if no index is specified).

fruits.pop(2)  # Removes the item at index 2
print(fruits)  # Output: ['apple', 'kiwi', 'orange', 'mango', 'pineapple']

fruits.pop()  # Removes the last item
print(fruits)  # Output: ['apple', 'kiwi', 'orange', 'mango']

# clear(): Removes all items from the list, making it empty.

fruits.clear()
print(fruits)  # Output: []

# Accessing Items in a List
# Use indexing to access specific items.

fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Output: 'apple'
print(fruits[-1])  # Output: 'cherry' (last item)
# Use slicing to access a range of items.

print(fruits[1:3])  # Output: ['banana', 'cherry'] (from index 1 up to, but not including,
# index 3)

# Other Useful List Methods
# index(): Finds the index of the first occurrence of a specified item.

position = fruits.index("banana")
print(position)  # Output: 1

# count(): Counts how many times an item appears in the list.
count = fruits.count("apple")
print(count)  # Output: 1
# sort(): Sorts the list in ascending order.
numbers = [5, 2, 9, 1]
numbers.sort()
print(numbers)  # Output: [1, 2, 5, 9]
# reverse(): Reverses the order of items in the list.

numbers.reverse()
print(numbers)  # Output: [9, 5, 2, 1]

# 6. Copying a List
# copy(): Creates a shallow copy of the list.
fruits_copy = fruits.copy()
print(fruits_copy)  # Output: ['apple', 'banana', 'cherry']

# 7. Looping Through a List
# Use a for loop to iterate through each item in the list.

for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry

# No, these operations do not apply to all other variable types in Python, as each data type has its own set of methods and characteristics. Here’s a breakdown of how lists, tuples, sets, and dictionaries differ in terms of supported operations.
#
# 1. List
# Characteristics: Ordered, changeable (mutable), allows duplicate items.
# Operations: You can add, remove, and modify items (methods like append, insert, remove, etc.).
# Accessing Items: By index (e.g., my_list[0]).