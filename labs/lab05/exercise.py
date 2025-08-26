# Basic input and output
print("Welcome to the Grade Calculator!")
print("This program will calculate your course grade.")

# Getting user input (always returns a string)
student_name = input("Hafiz ")
course_name = input("Sains Komputer")

# Getting numeric input requires conversion
assignment_score = float("80.0")
exam_score = float("80.0")
participation_score = float("60.0")

# Calculating final grade
final_grade = (assignment_score * 0.4) + (exam_score * 0.5) + (participation_score * 0.1)

# Formatted output using string concatenation
print()
print("Student: " + student_name)
print("Course: " + course_name)
print("Final Grade: " + str(final_grade) + "%")