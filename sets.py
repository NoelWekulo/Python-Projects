# 3. Set
# Description: A set is an unordered, changeable collection of unique items.
# Items in a set cannot be duplicated, and the set itself does not have a specific order.
# Syntax: Use curly braces {} to define a set.
# Example:
unique_numbers = {1, 2, 3, 3, 4}
print(unique_numbers)  # Output: {1, 2, 3, 4} (duplicates are removed)

# Adding an item
unique_numbers.add(5)
print(unique_numbers)  # Output: {1, 2, 3, 4, 5}

# Removing an item
unique_numbers.remove(3)
print(unique_numbers)  # Output: {1, 2, 4, 5}

# Real-World Analogy: A set is like a collection of people attending a party
# where each attendee’s name is unique, and there’s no specific order in which they arrive.

# 3. Set
# Characteristics: Unordered, no duplicate items, mutable.
# Operations: You can add and remove items, but sets do not support indexing or
# slicing (since they are unordered).
# Accessing Items: No specific order, so you cannot access items by index.
# Supported Methods:
# add: Adds an item to the set.
# remove/discard: Removes an item from the set. discard won’t raise an error if the item
# doesn’t exist, while remove will.
# union, intersection, difference: Perform set operations to combine or compare sets.
# Example:

my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}

# Union of sets
other_set = {3, 4, 5}
union_set = my_set.union(other_set)
print(union_set)  # Output: {1, 2, 3, 4, 5}
