# In Python, conditionals are used to make decisions in your code based on certain conditions. The main conditional statements in Python are if, elif, and else.
#
# Basic Conditional Structure
# if Statement: Checks if a condition is True and executes the code block if it is.
# elif (else if): Checks another condition if the previous if condition was False.
# else: Executes if none of the previous conditions were True.
# Example Structure
# if condition1:
#     # Code to run if condition1 is True
# elif condition2:
#     # Code to run if condition1 is False and condition2 is True
# else:
    # Code to run if neither condition1 nor condition2 is True
    # Examples
    # to
    # Illustrate
    # Example
    # 1: Checking if a
    # Number is Positive, Negative, or Zero

    number = 5

    if number > 0:
        print("The number is positive.")
    elif number < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")
# Explanation:
# If number is greater than 0, it will print "The number is positive."
# If number is less than 0, it will print "The number is negative."
# If neither condition is met (i.e., the number is 0), it will print "The number is zero."
# Example 2: Checking if Someone is Eligible to Vote
age = 18

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Explanation:
# If age is 18 or older, the program prints "You are eligible to vote."
# If age is less than 18, it prints "You are not eligible to vote."
# Using Multiple Conditions with Logical Operators
# You can combine conditions using logical operators like and, or, and not.
#
# and: Both conditions must be True for the code to run.
# or: At least one condition must be True for the code to run.
# not: Reverses the condition’s outcome (True becomes False, and vice versa).
# Example 3: Checking if a Number is in a Specific Range
number = 15

if number > 10 and number < 20:
    print("The number is between 10 and 20.")
else:
    print("The number is not between 10 and 20.")

In Python, conditionals are used to make decisions in your code based on certain conditions. The main conditional statements in Python are if, elif, and else.

Basic Conditional Structure
if Statement: Checks if a condition is True and executes the code block if it is.
elif (else if): Checks another condition if the previous if condition was False.
else: Executes if none of the previous conditions were True.
Example Structure
python
Copy code
if condition1:
    # Code to run if condition1 is True
elif condition2:
    # Code to run if condition1 is False and condition2 is True
else:
    # Code to run if neither condition1 nor condition2 is True
Examples to Illustrate
Example 1: Checking if a Number is Positive, Negative, or Zero
python
Copy code
number = 5

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
Explanation:
If number is greater than 0, it will print "The number is positive."
If number is less than 0, it will print "The number is negative."
If neither condition is met (i.e., the number is 0), it will print "The number is zero."
Example 2: Checking if Someone is Eligible to Vote
python
Copy code
age = 18

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
# Explanation:
# If age is 18 or older, the program prints "You are eligible to vote."
# If age is less than 18, it prints "You are not eligible to vote."
# Using Multiple Conditions with Logical Operators
# You can combine conditions using logical operators like and, or, and not.
#
# and: Both conditions must be True for the code to run.
# or: At least one condition must be True for the code to run.
# not: Reverses the condition’s outcome (True becomes False, and vice versa).
# Example 3: Checking if a Number is in a Specific Range

number = 15

if number > 10 and number < 20:
    print("The number is between 10 and 20.")
else:
    print("The number is not between 10 and 20.")

# Explanation:
# The and operator ensures that both conditions (number > 10 and number < 20) must be true for the message to print "The number is between 10 and 20."
# Example 4: Using or to Check for Multiple Valid Values

color = "blue"

if color == "red" or color == "blue":
    print("The color is either red or blue.")
else:
    print("The color is neither red nor blue.")
# Explanation:
# The or operator checks if color is "red" or "blue". If either condition is True, it prints the first message.
# Summary
# Use if to check a condition and run code only if it’s True.
# Use elif for additional conditions if the first if is False.
# Use else as a fallback if none of the previous conditions were True.
# Combine conditions using and, or, and not for more complex checks.