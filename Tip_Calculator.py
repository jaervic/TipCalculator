print("""
Welcome to the tip calculator by: Jaervic

This is a little project. Or as i like to call it, a little step more to a big goal.

""")

bill = float(input("What was the total?: $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?: "))
people = int(input("How many people is going to split the bill?: "))

# Convert the tip to a percentage dividing it by 100
tip_percent = tip / 100
# Amount that people are going to pay
total_amount = bill * tip_percent

total_bill = bill + total_amount

bill_per_person = total_bill / people

final_amount = round(bill_per_person, 2)

print(f'Your tip has to be {final_amount}.')