import employee_data

employee_data.basic_salary = 4500
employee_data.overtime_hours = 12   
employee_data.overtime_rate = 25

# Calculate these deductions 
EPF = 0.11
SOCSO = 0.005
EIS = 0.002
total_deductions = EPF + SOCSO + EIS

# Add fixed deductions
medical_insurance = 50
parking_fee = 30

# Calculate gross salary
overtime_pay = employee_data.overtime_hours * employee_data.overtime_rate
gross_salary = employee_data.basic_salary + overtime_pay
print(f"Gross Salary: RM {gross_salary}")

# Calculate each deduction
epf_deduction = employee_data.basic_salary * EPF
socso_deduction = employee_data.basic_salary * SOCSO
eis_deduction = employee_data.basic_salary * EIS
print(f"EPF Deduction: RM {epf_deduction}")
print(f"SOCSO Deduction: RM {socso_deduction}")
print(f"EIS Deduction: RM {eis_deduction}")

# Calculate total deductions
total_deductions_amount = epf_deduction + socso_deduction + eis_deduction + medical_insurance + parking_fee
print(f"Total Deductions: RM {total_deductions_amount}")

# Calculate net salary
net_salary = gross_salary - total_deductions_amount
print(f"Net Salary: RM {net_salary}")

