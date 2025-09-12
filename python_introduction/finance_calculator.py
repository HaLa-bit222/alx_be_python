income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))
monthly_savings = income - expenses
annual_savings = monthly_savings * 12
projected_savings = annual_savings * (1 + 0.05)
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}")
if monthly_savings > 0:
    savings_rate = (monthly_savings / income) * 100
    print(f"Your savings rate is {savings_rate:.1f}% of your income.")
else:
    print("Warning: You're spending more than you earn!")