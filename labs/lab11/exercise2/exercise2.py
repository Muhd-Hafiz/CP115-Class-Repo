num_days = int(input("Enter number of days: "))
danger_threshold = float(input("Enter danger threshold: "))

danger_days = 0
total_temp = 0

for i in range(num_days):
    temp = float(input(f"Enter temperature for day {i+1}: "))
    total_temp += temp
    
    if temp > danger_threshold:
        danger_days += 1

average_temp = total_temp / num_days

print(danger_days)
print(f"{average_temp:.1f}")
