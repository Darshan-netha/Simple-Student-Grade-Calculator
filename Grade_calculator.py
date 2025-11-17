# Student Grade Calculator
# Internship: Developers Arena - Data Science Domain
# Week 2 Project

# Taking user input
name = input("Enter the student's name: ")
marks = float(input("Enter the marks (out of 100): "))

# Determining grade based on marks
if marks >= 90:
    grade = "A"
    message = "Excellent work! Keep it up "
elif marks >= 75:
    grade = "B"
    message = "Great job! You're doing really well "
elif marks >= 60:
    grade = "C"
    message = "Good effort! Keep improving "
elif marks >= 40:
    grade = "D"
    message = "You passed, but there’s room to improve!"
else:
    grade = "F"
    message = "Don’t give up! Keep practicing and you’ll get there 💫"

# Displaying the result
print("\n==== Student Grade Report ====")
print(f"Student Name : {name}")
print(f"Marks Scored : {marks}")
print(f"Grade        : {grade}")
print(f"Feedback     : {message}")
