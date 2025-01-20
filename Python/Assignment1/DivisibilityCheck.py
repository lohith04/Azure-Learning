#Even Division Check

First_Number = int(input("Enter First Number to check divisibility: "))
Second_Number = int(input("Enter Second NUmber to check divisibility: "))
Remainder = Second_Number % First_Number
if(Remainder == 0):
    print(f"Given first number '{First_Number}' is divible by given second number '{Second_Number}'")
else:
    print(f"Given first number '{First_Number}' is not divible by given second number '{Second_Number}',and the Remainder is: {Remainder}")    

