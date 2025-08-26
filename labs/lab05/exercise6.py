total_minutes = int(input("Enter the time in minutes: "))

hours = total_minutes // 60
minutes = total_minutes % 60

print("\n--- Time Converter ---")
print(f"Original time: {total_minutes} minutes")
print(f"Converted time: {hours} hour(s) and {minutes} minute(s)")
