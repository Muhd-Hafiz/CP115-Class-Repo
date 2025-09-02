student_name = input("Enter student name: ")
gpa = float(input("Enter GPA (0.0-4.0): "))
credit_hours = int(input("Enter credit hours: "))

if gpa >= 3.8 and credit_hours >= 12:
    status = "Dean's List"
elif gpa >= 3.5 and credit_hours >= 12:
    status = "Honor Roll"
elif gpa >= 2.0:
    status = "Good Standing"
elif gpa < 2.0:
    status = "Probation"
else: # credit_hours < 12
    status = "cannot qualify for dean's list or honor roll due to insufficient credit hours" \
    
print(f"\nStudent: {student_name}")
print(f"GPA: {gpa}")
print(f"Credit Hours: {credit_hours}")
print(f"Status: {status}")