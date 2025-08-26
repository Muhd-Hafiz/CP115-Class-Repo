import menu_data

menu = [menu_data.menu_item1, menu_data.menu_item2, menu_data.menu_item3]
daily_special = menu[menu_data.daily_special_number - 1]

print(f"Welcome to {menu_data.restaurant_name}!")
print(f"Location: {menu_data.restaurant_location}")
print(f"Customer No: {menu_data.customer_number}")

print(f"\nMenu:")
print(f"1. {menu_data.menu_item1}")
print(f"2. {menu_data.menu_item2}")
print(f"3. {menu_data.menu_item3}")

print(f"\nToday's Special: {daily_special}")
