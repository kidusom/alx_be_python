income = float(input("Enter your monthly income:"))

expenses = float(input("Enter your total monthly expenses: "))

savings = income - expenses

annual_savings = savings * 12
projected_saving = annual_savings + (annual_savings * 0.05)
projected_savings = int(projected_saving)
 
print(f"Your monthly savings are: {savings}")
print(f"Your projected annual savings after including interest are: {projected_savings}")