#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇 

print("Welcome to the Tip Calculator!") 

total_bill = float(input("What was the total bill? $"))
percent_tip = float(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
num_of_people = int(input("How many people to split the bill?\n"))

# total_tip_amount = total_bill * (percent_tip / 100)  **This is just to see the tip amount

final_after_tip = round(total_bill * (percent_tip / 100 + 1), 2)

final_bill_split = round(final_after_tip / num_of_people, 2)

individual_bill = f"Each person should pay: ${final_bill_split:.2f}."


print(individual_bill)
