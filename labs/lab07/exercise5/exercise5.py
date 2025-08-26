import personal_data

print("=== Personal Profile ===")
print(f"Name     : {personal_data.full_name}")
print(f"Age      : {personal_data.age}")
print(f"Height   : {personal_data.height_cm} cm")
print(f"Weight   : {personal_data.weight_kg} kg")
print(f"Phone    : {personal_data.phone_number}")
print(f"Email    : {personal_data.email}")

print("\n=== String Processing ===")
print(f"Name (UPPER)   : {personal_data.full_name_upper}")
print(f"Name (lower)   : {personal_data.full_name_lower}")
print(f"Name Length    : {personal_data.full_name_length}")
print(f"First Name     : {personal_data.first_name}")
print(f"City (UPPER)   : {personal_data.city_upper}")

print("\n=== Address Info ===")
print(f"Full Address   : {personal_data.full_address}")
print(f"Address Length : {personal_data.full_address_length}")
