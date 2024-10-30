# This code solves a student grading or marks management problem, where the user
# inputs marks for various subjects, and the code calculates the total marks and average
# marks across these subjects. Here’s how it addresses this problem:
#
# Problem Statement: Student Marks Entry and Grade Calculation
# Goal: Create a function that:
#
# Prompts the user to enter the number of subjects.
# For each subject:
# Asks for the subject's name.
# Prompts the user to enter the marks, validating that they are integers within the range of
# 0 to 100.
# Calculates:
# The total marks for all subjects.
# The average marks.
# Outputs a dictionary containing each subject with its marks, along with the total and average
# marks.
# Key Operations in the Code
# User Input: Collects the number of subjects, subject names, and their respective marks.
# Validation: Ensures that marks are integers between 0 and 100.
# Calculation:
# Computes the total marks by summing up all subject marks.
# Calculates the average by dividing the total by the number of subjects.
# Output: Displays a summary containing:
# Each subject’s name with its marks.
# The total and average marks.

def addMarks():
    total_marks = 0  # Initialize total marks
    subjects = {}    # Dictionary to store subjects and marks

    def recordMarks(noOfSubjects):
        total = 0  # Local variable to hold the sum of marks

        # Loop to enter subject names and marks
        for i in range(1, noOfSubjects + 1):
            name = input(f"Enter the name of subject {i}: ")

            # Input and validate marks
            while True:
                try:
                    marks = int(input(f"Enter the marks of subject {i}: "))
                    if 0 <= marks <= 100:
                        break
                    else:
                        print("The marks should range between 0 and 100.")
                except ValueError:
                    print("The marks should be an integer.")

            # Store the subject and its marks
            subjects[name] = marks
            total += marks  # Add to total

        return total  # Return total marks

    def calculate_grade(average):
        # Determine grade based on average marks
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'

    try:
        # Input number of subjects
        noOfSubjects = int(input("Enter number of subjects: "))
        total_marks = recordMarks(noOfSubjects)  # Calculate total marks

        # Calculate average and store total/average in dictionary
        average = total_marks / len(subjects)
        grade = calculate_grade(average)  # Get grade based on average

        # Add results to subjects dictionary
        subjects["Total marks"] = total_marks
        subjects["Average"] = int(average)
        subjects["Grade"] = grade

        # Print result
        print(subjects)

    except ValueError:
        print("The number of subjects must be an integer.")
        exit()

# Call the function to run the code
addMarks()

