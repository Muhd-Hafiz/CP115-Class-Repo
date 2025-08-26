grade1 = 78
grade2 = 85
grade3 = 92
grade4 = 67
grade5 = 88
full_marks = 100
total_marks = full_marks * 5

# calculate total grade
total_grade = grade1 + grade2 + grade3 + grade4 + grade5
print(f"Total grade: {total_grade}/{total_marks} (type: {type(total_grade)})")

# Calculate average grade
average_grade = (grade1 + grade2 + grade3 + grade4 + grade5)/5
print(f"Average grade: {average_grade} (type: {type(average_grade)})")

# Calculate percentage each test
percentage1 = (grade1 / full_marks) * 100
percentage2 = (grade2 / full_marks) * 100   
percentage3 = (grade3 / full_marks) * 100
percentage4 = (grade4 / full_marks) * 100   
percentage5 = (grade5 / full_marks) * 100
print(f"Percentage for each test: {percentage1}%, {percentage2}%, {percentage3}%, {percentage4}%, {percentage5}%")
