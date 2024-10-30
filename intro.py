print("Our first python program")

# python is case sensitive
# python takes indentation seriously
# comments=====ctrl+/
# variables cannont have spaces use underscore _ instead

#In Python, variables are containers for storing data values. Variables do not need to
# be declared with any specific type and can change type after being set. Here’s a
# reakdown of all the major types of variables (also called data types) you’ll
# encounter in Python, with examples of how to use them:

# # Integer (int)
# Description: Whole numbers, both positive and negative, without a decimal point.
# Example:
# python
#
# x = 10   # integer
# y = -5   # negative integer

# 2. Floating-Point (float)
# Description: Numbers that contain decimal points. Can represent both integers and
# real numbers.
# Example:
# python
#
# pi = 3.14  # float
# z = -0.01  # negative float

# 3. String (str)
# Description: A sequence of characters enclosed in single (') or double (") quotes.
# Example:
# python
#
# name = "Alice"  # string with double quotes
# greeting = 'Hello'  # string with single quotes

# 4. Boolean (bool)
# Description: Represents either True or False.
# Example:
# python
#
# is_active = True   # boolean
# is_logged_in = False  # boolean

# 5. List
# Description: An ordered, mutable (changeable) collection of items. Items can be of
# different types.
# Example:
# python
#
# numbers = [1, 2, 3, 4, 5]  # list of integers
# mixed_list = [1, "apple", 3.14, True]  # mixed data types

# 6. Tuple
# Description: An ordered, immutable collection of items. Items can be of different types.
# Example:
#
#
# coordinates = (10, 20)  # tuple of integers
# person = ("Alice", 25)  # tuple with mixed types

# 7. Dictionary (dict)
# Description: A collection of key-value pairs. Keys are unique, and each key maps to a
# specific value.
# Example:
# python
# C
# person = {
#     "name": "Alice",
#     "age": 30,
#     "is_student": False
# }
# 8. Set
# Description: An unordered collection of unique elements.
# Example:
# python
#
# fruits = {"apple", "banana", "cherry"}  # set of strings
# unique_numbers = {1, 2, 3, 3, 4}  # duplicates are removed

# 9. NoneType
# Description: Represents the absence of a value or a null value. The only value of this type is None.
# Example:
# python
#
# result = None  # none type

# 10. Complex
# Description: Used to represent complex numbers. It is written with a real part and an imaginary part.
# Example:
# python
#
# complex_number = 1 + 2j  # complex number with real part 1 and imaginary part 2

# 11. Bytes
# Description: A sequence of bytes. Used for binary data.
# Example:
# python
# Copy code
# byte_data = b"hello"  # bytes

# 12. Bytearray
# Description: A mutable sequence of bytes.
# Example:
# python
# Copy code
# byte_array_data = bytearray(b"hello")  # bytearray
# byte_array_data[0] = 104  # modifying the first byte

# 13. Range
# Description: Represents a sequence of numbers, commonly used in loops.
# Example:
# python
# Copy code
# for i in range(5):  # generates numbers from 0 to 4
#     print(i)
# Example Usage
# Let’s create a simple program that uses a variety of these variables:
#
# python
# Copy code
# name = "Bob"  # String
# age = 30  # Integer
# height = 5.9  # Float
# is_adult = True  # Boolean
# skills = ["Python", "JavaScript", "SQL"]  # List
# address = ("123 Main St", "City", "Country")  # Tuple
# person_info = {"name": "Bob", "age": 30, "skills": skills}  # Dictionary
# unique_values = {1, 2, 3, 4}  # Set
# complex_num = 3 + 4j  # Complex number
# byte_string = b"example"  # Bytes
# byte_array = bytearray(b"example")  # Bytearray
# empty_value = None  # NoneType
#
# print(f"{name} is {age} years old, {height} feet tall, and skilled in {skills[0]}.")
# Summary:
# Python supports multiple variable types, and it handles them dynamically (no need to
# declare the type). Each type is useful in different scenarios,
# such as storing data in different formats, manipulating text, processing
# numbers, etc.