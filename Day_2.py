print("Welcome to the tip calculator.")
bill = float(input("what is your total bill?\n$"))
peoples = int(input("How many peoples to split the bill\n"))
tip = int(input("What percentage of tip would you like to give? 10 ,12 or 15?\n"))
tip_percentage = tip / 100
total_tip = bill * tip_percentage 
total_bill =  bill + total_tip
on_each = total_bill / peoples
final_amount = "{:.2f}".format(on_each)
print(f"Each person should pay ${final_amount}")