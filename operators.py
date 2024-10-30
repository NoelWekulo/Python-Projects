maths=70
kisw=60
science=55
english=90
total=maths+kisw+science+english
mean_score=total/4
print(total)
print(mean_score)

max_marks=500
total_marks=255
remaining_marks=max_marks-total_marks
print(remaining_marks)


# #Create variables to store two numbers (e.g., num1 = 15 and num2 = 7).
#
# Perform the following operations using these variables and print the results:
#
# Addition
# Subtraction
# Multiplication
# Division
# Exponentiation (raise one number to the power of the other)

num1=15
num2=10
addition=num1+num2
subtraction=num1-num2
multiplication=num1*num2
division=num1/num2
quotient=num1%num2
exponential=num1**num2
print(addition,subtraction,multiplication,division,quotient,exponential)
# Task 1.2: String Manipulation
# Create a string variable with your full name.
#
# Perform the following string operations:
#
# Convert the string to all uppercase.
# Convert the string to all lowercase.
# Find and print the length of your name.
# Extract and print the first three characters of your name.

full_name="Noel Wekulo"
print(full_name.upper())
print(full_name.lower())
print(full_name.capitalize())
print(len(full_name))
print(full_name[:3])

# Task 1.3: Variable Reassignment and Type Conversion
# Create a variable that stores a person's age as an integer (e.g., age = 25).
#
# Convert the integer to a string and concatenate it with a message like "My age is 25."
#
# Reassign the age variable with a floating-point value (e.g., age = 25.5) and print it.
#
# Convert the floating-point age back to an integer.
age=30
age_string=str(age)
print(f"my age is {age_string}")

age=20.5
print(age)

age=int(age)
print(age)
# Task 1.4: Temperature Conversion
# Create a variable to store a temperature in Celsius (e.g., temp_celsius = 25).
#
# Convert the temperature to Fahrenheit using the formula:
# fahrenheit = (celsius * 9/5) + 32
#
# Print the result with a message like "The temperature in Fahrenheit is X."

temp_celsius=25
fahrenheit = (temp_celsius * 9/5) + 32
X=fahrenheit
print(f"The temperature in Fahrenheit is {X}")

# Task 1.5: Area and Perimeter of a Rectangle
# Create two variables length and width to store the dimensions of a rectangle.
#
# Calculate the area (length * width) and the perimeter (2 * (length + width)).
#
# Print the results with descriptive messages.

length=10
width=5
Area=length*width
perimeter=2*(length+width)
print(f"the area of the rectangle is {Area} and the perimeter is {perimeter}")

# Challenge Task (Optional)
# Create a variable to store a person's weight in kilograms (e.g., weight_kg = 70).
# Write code to convert the weight into pounds (use the formula: pounds = kilograms * 2.20462).
# Print both the weight in kilograms and the weight in pounds.

p1_weight_kg=70
pounds = p1_weight_kg * 2.20462
print(f"The weight in kg is {p1_weight_kg} while the weight in pound is {pounds:.2f}")
