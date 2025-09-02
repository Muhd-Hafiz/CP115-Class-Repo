employee_name = input("Enter employee name: ")
base_salary = float(input("Enter base salary: "))
overtime_hours = int(input("Enter overtime hours worked: "))
tax_status = input("Enter tax status (single/married/head): ").strip().lower()

overtime_per_hours = 35
additional_deductions = 0.16

if tax_status == "single" and "base_salary >= 5000":
    tax_rate = 0.22
elif tax_status == "single" and base_salary <= 5000:
    tax_rate = 0.18
elif tax_status == "married" and base_salary >= 6000:
    tax_rate = 0.20
elif tax_status == "married" and base_salary <= 6000:
    tax_rate = 0.15
elif tax_status == "head" and base_salary >= 5500:
    tax_rate = 0.25
elif tax_status == "head" and base_salary <= 5500:
    tax_rate = 0.19 
else:
    tax_rate = 0.0

# calculate total tax and sallary

total_tax = (base_salary * tax_rate) + (base_salary * additional_deductions)
overtime_pay = overtime_hours * overtime_per_hours
net_salary = base_salary + overtime_pay - total_tax

print("\nEmployee Payroll Summary")
print(total_tax)
print(overtime_pay)
print(net_salary)
    




