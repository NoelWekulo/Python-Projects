# 1. What is a Function?
# A function is a block of code that performs a specific task.
# Functions help you avoid repetition by letting you call the same code multiple times with different inputs.
# In Python, functions are defined using the def keyword.
# 2. Defining a Function
# You define a function with the def keyword, followed by the function name and parentheses ().
# If the function needs input, you specify parameters inside the parentheses.
# The code inside the function is indented.
# Syntax:

def function_name(parameters):
    # code block
    return result


def greet (name):
    print(f"Hello,{name}!")
greet("Noel")

# write a function to add two numbers and display results

def add(a,b):
    return a+b
result= add(3,5)
print(result)

def greet(name="guest"):
    print(f"Hello,{name}!")
greet()
greet("Noel")
# write a python program to introduce yourself with name and age
def introduce(name,age):
    print(f"Hello am {name} and iam {age} years old")
introduce(age=25,name='noel')

# *args and **kwargs for Variable Arguments
def add(*numbers):
    return sum(numbers)

print(add(1, 2, 3))

def describe_person(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

describe_person(name="Alice", age=30, job="Engineer")

# 10. Scope of Variables in Functions
# Local Scope: Variables created inside a function are local to that function and can’t
# be accessed outside of it.
# Global Scope: Variables created outside all functions are global and can be accessed
# from any part of the code.
# Example:

x = 10  # Global variable

def test_scope():
    x = 5  # Local variable
    print(x)  # Output: 5

test_scope()
print(x)  # Output: 10 (global x remains unchanged)

# 11. Lambda Functions
# Lambda functions are anonymous, one-line functions defined using the lambda keyword.
# They are typically used for short, simple operations.
# Example:
square = lambda x: x ** 2
print(square(4))  # Output: 16

# 12. Docstrings
# Docstrings are used to document what a function does and can be accessed with help() or __doc__.
# Example:
def add(a, b):
    """Adds two numbers and returns the result."""
    return a + b

print(add.__doc__)  # Output: Adds two numbers and returns the result.

# 13. Higher-Order Functions
# A function that takes other functions as parameters or returns a function as a result.
# Example:

def apply_function(func, value):
    return func(value)

print(apply_function(lambda x: x * 2, 5))  # Output: 10

# Summary
# Define functions with def.
# Call functions by their name.
# Use parameters in definitions and pass arguments in calls.
# Use return to get output from a function.
# Leverage default arguments, *args, and **kwargs for flexible functions.
# Understand scope and docstrings for clarity.
# Explore lambda functions and higher-order functions for advanced uses.
