item_name = input("Enter the item name: ")
price = float(input("Enter the price of one item: $"))

quantity = 3
tax_rate = 0.06  # 6%

subtotal = price * quantity
tax_amount = subtotal * tax_rate
total_cost = subtotal + tax_amount

print("\n--- Shopping Cost Summary ---")
print(f"Item: {item_name}")
print(f"Price per item: ${price:.2f}")
print(f"Quantity: {quantity}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (6%): ${tax_amount:.2f}")
print(f"Total Cost: ${total_cost:.2f}")

