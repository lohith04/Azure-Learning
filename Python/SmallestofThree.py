#Smallest of Three Numbers

First_Number = int(input("Enter First Number: "))
Second_Number = int(input("Enter Second Number: "))
Third_Number = int(input("Enter Third Number: "))
Smallest_Number = Third_Number if Third_Number < First_Number else First_Number if First_Number < Second_Number else Second_Number
print(f"Smallest number out of given three numbers is: {Smallest_Number}!")