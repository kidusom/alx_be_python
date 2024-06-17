income = int(input("Enter your monthly income:"))

expenses = int(input("Enter your total monthly expenses: "))

savings = income - expenses

annual_savings = savings * 12
projected_savings = annual_savings + (annual_savings * 0.05)
 
print(f"Your monthly savings are: {savings}")
print(f"Your projected annual savings after including interest are: {projected_savings}")