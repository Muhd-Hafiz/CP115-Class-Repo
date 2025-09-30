monthly_usage = float(input())

# Determine discount rate based on monthly usage
discount = 0

if monthly_usage < 50:
    discount = 0
elif monthly_usage <= 100:
    discount = 0.05
elif monthly_usage > 100:
    discount = 0.20

#Calculate total bill after applying discount
total_bill = monthly_usage * (1 - discount)

print(float(total_bill))
