import random 

class_name = input("Enter your class name: ")

random_student_id = random.randint(1, 30)

print("\n--- Random Student Selector ---")
print(f"Class: {class_name}")
print(f"Selected Random Student ID: {random_student_id}")
