import math

number = float(input("Enter a number: "))

square_root = math.sqrt(number)
square = number ** 2
cube = number ** 3
sine_value = math.sin(number) 

print("\n--- Advance Math Calculations ---")
print(f"Square root of {number}: {square_root}")
print(f"Square of {number}: {square}")
print(f"Cube of {number}: {cube}")
print(f"Sine of {number} (in radians): {sine_value}")