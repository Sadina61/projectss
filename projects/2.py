#project no 2[ Tip calculator ]
print("Welcome to the Tip Calculator")
bill=input("What was the total bill? $")
tip=input("What percentage tip would you like to give ? 10, 12 or 15 ")
people=input("How many people to split the bill ? ")
Total= (float(bill)+ (int(tip)/100)*float(bill))/int(people)
Final=round(Total,2)
print(f"Each person should pay ${Final}")