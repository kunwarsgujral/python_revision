print("Welcome to the tip calculator.")
total_bill_amount = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
bill_with_tip = tip / 100 * total_bill_amount + total_bill_amount
split_bill_into = int(input("How many people to split the bill? "))
total_for_each_person = (bill_with_tip)/ split_bill_into 
total_for_each_person = round(total_for_each_person, 2)
print(f"Each person should pay: ${total_for_each_person}")
