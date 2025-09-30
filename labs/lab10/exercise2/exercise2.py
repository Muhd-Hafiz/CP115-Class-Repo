age = int(input())
accident_count = int(input())

base_premium = 0

if age < 25:
    base_premium = 2400
elif 25 <= age <= 40:
    base_premium = 1800
elif age > 50:
    base_premium = 2000

accident_count = 0 
final_premium = 0

if accident_count == 0:
    final_premium = base_premium
elif accident_count == 1 and accident_count == 2:
    final_premium = base_premium + 300
elif accident_count > 2:
    final_premium = base_premium + 600

if accident_count == 0:
    discount_amount = base_premium * 0.10
    final_premium = base_premium - discount_amount
else:
    discount_amount = 0

final_premium = int(final_premium)
discount_amount = int(discount_amount)

print(base_premium)
print(final_premium)
print(discount_amount)