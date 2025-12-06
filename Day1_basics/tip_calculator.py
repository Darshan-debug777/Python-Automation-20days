
bill = float(input("Enter total bill amount: ₹"))

tip_percent = float(input("Enter tip percentage (e.g., 10 for 10%): "))

tip_amount = (bill * tip_percent) / 100

total = bill + tip_amount


print(f"Tip amount: ₹{tip_amount:.2f}")
print(f"Total amount to pay: ₹{total:.2f}")
