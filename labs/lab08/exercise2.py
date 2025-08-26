# Prices
main_dish_price = 25
appetizer_price = 12
drink_price = 8

# Quantities
main_dish_qty = 3
appetizer_qty = 2
drink_qty = 4

# Friends
num_friends = 6

# ( (Food cost + Drinks + Appetizers) + Delivery ) + Tax
subtotal = (main_dish_price * main_dish_qty) + (appetizer_price * appetizer_qty) + (drink_price * drink_qty)

# Total with tax and delivery using brackets to respect BODMAS
total_bill = (subtotal + 5) + ((subtotal + 5) * 0.10)

# Each person’s share, floor division to ignore cents
per_person = total_bill // num_friends

print("Subtotal (before tax & delivery): RM", subtotal)
print("Total bill (with tax & delivery): RM", total_bill)
print("Each person needs to pay: RM", per_person)
print("Note: Each person pays RM", total_bill / num_friends, "if cents are included.")


