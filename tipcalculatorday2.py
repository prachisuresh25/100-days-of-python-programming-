print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip=tip_percentage/100
total_tip=tip*bill
bill_per_person=((bill+total_tip)/people)
final_ans=round(bill_per_person, 2)
print(final_ans)


