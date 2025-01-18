#Check Eligibility to Vote

Age = int(input("Enter Age of the person to Check Eligibility to Vote: "))
if (Age > 100 or Age < 1):
    print("Enter Valid age!")
elif (Age >= 18):
    print("Eligible to vote!")    
else:
    print("Not Eligible to vote!") 