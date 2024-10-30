# write a Python program for a grading system that calculates
# the average of multiple scores and assigns a grade based on the average:

# Get scores from the user
score1 = float(input("Enter score for subject 1: "))
score2 = float(input("Enter score for subject 2: "))
score3 = float(input("Enter score for subject 3: "))
score4 = float(input("Enter score for subject 4: "))
score5 = float(input("Enter score for subject 5: "))

# Calculate the average score
average_score = (score1 + score2 + score3 + score4 + score5) / 5

# Determine the grade based on the average score
if average_score >= 90:
    grade = 'A'
elif average_score >= 80:
    grade = 'B'
elif average_score >= 70:
    grade = 'C'
elif average_score >= 60:
    grade = 'D'

elif average_score >= 40:
    grade = 'E'
else:
    grade = 'F'

# Print the average score and grade
print(f"Average score: {average_score}")
print(f"Grade: {grade}")
