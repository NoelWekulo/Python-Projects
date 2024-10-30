# 2. Tuple
# Description: A tuple is an ordered, unchangeable collection of items.
# Once you create a tuple, you cannot modify its contents (no adding, removing, or
# changing items).
# Syntax: Use parentheses () to define a tuple.
# Example:

colors = ("red", "green", "blue")
print(colors)  # Output: ('red', 'green', 'blue')

# Accessing an item
print(colors[0])  # Output: 'red'

# Trying to change an item (will cause an error)
# colors[1] = "yellow"  # Error: 'tuple' object does not support item assignment

# Real-World Analogy: A tuple is like a phone number (area code, prefix, line number).
# It’s fixed, so once assigned,
# it typically doesn’t change.

# 2. Tuple
# Characteristics: Ordered, unchangeable (immutable), allows duplicate items.
# Operations: Limited compared to lists. Once a tuple is created, you cannot add, remove, or change items.
# Accessing Items: By index (e.g., my_tuple[1]).
# Supported Methods: Tuples have fewer methods, mainly count (to count occurrences of a value) and
# index (to find the position of a value).

my_tuple = (1, 2, 3)
print(my_tuple.count(2))  # Output: 1
print(my_tuple.index(3))  # Output: 2
