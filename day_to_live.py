age =  input("What is your current age? ")
time_to_live =  90 - int(age) 
time_to_live_in_days = time_to_live * 365
time_to_live_in_weeks = time_to_live * 52
time_to_live_in_months = time_to_live *12 
print(f"You have {time_to_live_in_days} days to live,{time_to_live_in_weeks} weeks, and {time_to_live_in_months} months left")

