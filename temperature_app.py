# 1. Temperature Conversion App
# • Write a set of functions to convert between Celsius, Fahrenheit, and Kelvin
# temperature scales.
# • Include input validation to ensure valid temperature values.

# Step 1: Understand the Conversion Requirements
# The goal is to create functions that convert temperatures between three scales:
#
# Celsius (C)
# Fahrenheit (F)
# Kelvin (K)
# Each scale has specific formulas for converting to the other two, so we'll need to understand
# these formulas first.
#
# Step 2: Conversion Formulas
# To convert between temperature scales, we need to use the following formulas:
#
# Celsius to Fahrenheit: F = C * 9/5 + 32
# Celsius to Kelvin: K = C + 273.15
# Fahrenheit to Celsius: C = (F - 32) * 5/9
# Fahrenheit to Kelvin: K = (F - 32) * 5/9 + 273.15
# Kelvin to Celsius: C = K - 273.15
# Kelvin to Fahrenheit: F = (K - 273.15) * 9/5 + 32
# These formulas will be the core of our conversion functions.
#
# Step 3: Define the Functions for Each Conversion
# We’ll create individual functions to handle each conversion. This way, each function will
# have a single responsibility, making the code modular and easy to understand.
#
# Example Functions:
# celsius_to_fahrenheit(celsius): Converts Celsius to Fahrenheit.
# fahrenheit_to_kelvin(fahrenheit): Converts Fahrenheit to Kelvin.
# And so on for each pair of conversions.
# Step 4: Input Validation
# In temperature scales, there are certain limits:
#
# Absolute Zero: This is the lowest possible temperature, where particles have minimal energy.
# Celsius: Absolute zero is -273.15 °C.
# Fahrenheit: Absolute zero is -459.67 °F.
# Kelvin: Absolute zero is 0 K.
# Since temperatures cannot go below these values, our program should include input validation:
#
# If the temperature in Celsius is below -273.15, Fahrenheit below -459.67, or Kelvin below 0,
# we should not perform the conversion and instead inform the user that the temperature is
# invalid.
# Step 5: Create a Main Function to Handle User Interaction
# Get User Input:
#
# Prompt the user to enter the temperature they wish to convert.
# Prompt for the current scale (Celsius, Fahrenheit, or Kelvin).
# Prompt for the target scale (the scale they want to convert to).
# Perform the Conversion:
#
# Use the functions defined in Step 3 to perform the appropriate conversion based on the input.
# Ensure the input temperature is valid for the specified scale.
# Display the Result:
#
# Output the converted temperature to the user with a clear message indicating the new scale.
# Step 6: Example Flow of the Program
# Here’s an example of how the program should work from start to finish:
#
# User Input:
#
# The user enters a temperature (e.g., 25).
# The user specifies the current scale as Celsius (C).
# The user specifies the target scale as Fahrenheit (F).
# Program Logic:
#
# The program checks if the input is valid (e.g., 25 °C is valid).
# It then converts 25 °C to Fahrenheit using the formula F = C * 9/5 + 32, which gives 77 °F.
# Output:
#
# The program displays: "The temperature in F is: 77.0".
# Summary of Steps
# Define Conversion Functions for each pair of temperature scales using the formulas.
# Validate Input to ensure temperatures are above absolute zero for each scale.
# Create a Main Function to interact with the user:
# Get input for the temperature, current scale, and target scale.
# Use the appropriate conversion function to calculate the result.
# Display the result.

def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

# Step 4: Input Validation
# In temperature scales, there are certain limits:
#
# Absolute Zero: This is the lowest possible temperature, where particles have minimal energy.
# Celsius: Absolute zero is -273.15 °C.
# Fahrenheit: Absolute zero is -459.67 °F.
# Kelvin: Absolute zero is 0 K.
# Since temperatures cannot go below these values, our program should include input validation:
#
# If the temperature in Celsius is below -273.15, Fahrenheit below -459.67, or Kelvin below 0,
# we should not perform the conversion and instead inform the user that the temperature is
# invalid.

def is_valid_temperature(temp, scale):
    # Validate temperature ranges based on scale
    if scale == "C" and temp >= -273.15:
        return True
    elif scale == "F" and temp >= -459.67:
        return True
    elif scale == "K" and temp >= 0:
        return True
    return False


def convert_temperature(temp, from_scale, to_scale):
    if not is_valid_temperature(temp, from_scale):
        return "Invalid temperature value for the given scale."

    if from_scale == "C":
        if to_scale == "F":
            return celsius_to_fahrenheit(temp)
        elif to_scale == "K":
            return celsius_to_kelvin(temp)
    elif from_scale == "F":
        if to_scale == "C":
            return fahrenheit_to_celsius(temp)
        elif to_scale == "K":
            return fahrenheit_to_kelvin(temp)
    elif from_scale == "K":
        if to_scale == "C":
            return kelvin_to_celsius(temp)
        elif to_scale == "F":
            return kelvin_to_fahrenheit(temp)

    return "Invalid scale conversion. Please ensure 'C', 'F', or 'K' are used."
# #Step 5: Create a Main Function to Handle User Interaction
# Get User Input:
#
# Prompt the user to enter the temperature they wish to convert.
# Prompt for the current scale (Celsius, Fahrenheit, or Kelvin).
# Prompt for the target scale (the scale they want to convert to).
# Perform the Conversion:
#
# Use the functions defined in Step 3 to perform the appropriate conversion based on the input.
# Ensure the input temperature is valid for the specified scale.
# Display the Result:
#
# Output the converted temperature to the user with a clear message indicating the new scale.

# Main function to interact with the user
def temperature_conversion_app():
    print("Welcome to the Temperature Conversion App!")
    try:
        temp = float(input("Enter the temperature you want to convert: "))
    except ValueError:
        print("Invalid input. Please enter a numeric temperature.")
        return  # Exit if input is invalid

    from_scale = input("Enter the current scale (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()
    to_scale = input("Enter the target scale (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()

    # Validate scale inputs
    if from_scale not in {"C", "F", "K"} or to_scale not in {"C", "F", "K"}:
        print("Invalid scale input. Please use 'C', 'F', or 'K' only.")
        return  # Exit if scales are invalid

    # Perform conversion and display result
    result = convert_temperature(temp, from_scale, to_scale)
    if isinstance(result, str):  # If the result is an error message
        print(result)
    else:
        print(f"The temperature in {to_scale} is: {result:.2f}")


# Run the app
temperature_conversion_app()