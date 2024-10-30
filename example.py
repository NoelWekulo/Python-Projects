# Exercise 1: Simple Greeting Function
# Write a function called greet that takes a name as an argument and prints a greeting message.
# If no name is provided, it should greet "Guest" by default.

def greet(name="guest"):
    print(f"Hello, {name}")

greet("Noel")
greet()

# Exercise: Simple Age Check Function
# Write a function called check_age that takes a name and age as arguments.
# If the age is not provided, it should default to 18. The function should print a message
# saying whether the person is an adult (18 or older) or not.
#
# Requirements
# If the age is 18 or above, print "<name> is an adult."
# If the age is below 18, print "<name> is not an adult."
# If no age is provided, assume the age is 18.

def check_age(name,age=18):
    if age>18:
        print(f"{name} is an adult")
    elif age<18:
        print(f"{name} is not an adult")
    else:
        print(f"{name} is 18")

check_age(name="Noel",age=25)
check_age(name="Haven",age=16)
check_age(name="Noel")
# Exercise: Simple Temperature Converter
# Write a function called convert_temperature that takes a temperature and a unit as arguments.
# The unit can be either "C" for Celsius or "F" for Fahrenheit. If no unit is provided, assume the temperature is in Celsius.
#
# If the unit is "C", convert the temperature to Fahrenheit.
# If the unit is "F", convert the temperature to Celsius.
# Use the following formulas:
#
# Celsius to Fahrenheit: F = C * 9/5 + 32
# Fahrenheit to Celsius: C = (F - 32) * 5/9
# Requirements
# The function should print the converted temperature with a message indicating the new unit.


def convert_temperature(temp,unit="C"):
    if unit=="C":
        converted_temp= temp*9/5+32

        print(f"the {temp} in C is converted to {converted_temp} F")
    elif unit=="F":
        converted_temp = (temp-32)*5/9
        print(f"the {temp} in F is converted to {converted_temp} C")

    else:
        print(f"the {temp} in C")

convert_temperature(50,"F")
convert_temperature(77,'C')
convert_temperature(50)
convert_temperature(100,'K')





