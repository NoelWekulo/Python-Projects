# 4. Dictionary
# Description: A dictionary is an unordered, changeable collection of key-value pairs.
# Each item in a dictionary has a unique key and an associated value, like a label and its data.
# Syntax: Use curly braces {} with key-value pairs separated by a colon :.
# Example:
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(person)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Accessing a value by key
print(person["name"])  # Output: 'Alice'

# Adding a new key-value pair
person["job"] = "Engineer"
print(person)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'job': 'Engineer'}

# Real-World Analogy: A dictionary is like a contact book,
# where each contact (key) has associated details(values) like their phone number, email,
# or address.

# 4. Dictionary
# Characteristics: Unordered (in older Python versions), key-value pairs, mutable.
# Operations: You can add, remove, and modify key-value pairs.
# Accessing Items: By key (e.g., my_dict["key"]).
# Supported Methods:
# get: Retrieves the value for a specified key.
# update: Updates the dictionary with key-value pairs from another dictionary or iterable.
# pop: Removes a key-value pair by key.
# keys, values, items: Return collections of keys, values, or both.
# Example:
my_dict = {"name": "Alice", "age": 25}
print(my_dict.get("name"))  # Output: 'Alice'

# Adding a new key-value pair
my_dict["city"] = "New York"
print(my_dict)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Removing an item by key
my_dict.pop("age")
print(my_dict)  # Output: {'name': 'Alice', 'city': 'New York'}
