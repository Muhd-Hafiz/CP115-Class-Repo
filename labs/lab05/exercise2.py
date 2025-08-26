import math

radius = float(input("Enter the radius of the circle: "))

area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print("\n--- Circle Calculations ---")
print("Area: ", str(area))
print("Circumference: ", str(circumference))
print("Radius: ", str(radius))