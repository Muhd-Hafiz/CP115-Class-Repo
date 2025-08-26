membership_per_month = 120
personal_training_session = 80
book_session = 6
locker_rental = 25
towel_service = 15
registration_new_member = 50

# Calculate total first month cost for new member with all services
total_first_month = (membership_per_month + (personal_training_session * book_session) + locker_rental + towel_service + registration_new_member)
print(f"Total first month cost for new member with all services: RM {total_first_month}")

# Calculate monthly cost after first month without registration new member fee
total_monthly_after_first = (membership_per_month + (personal_training_session * book_session) + locker_rental + towel_service)
print(f"Monthly cost after first month without registration fee: RM {total_monthly_after_first}")

# Calculate total cost for 12 month including first month
total_cost_12_months = total_first_month + (total_monthly_after_first * 11)
print(f"Total cost for 12 months including first month: RM {total_cost_12_months}")
