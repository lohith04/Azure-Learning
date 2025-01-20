#Find the Maximum

First_Number = int(input("Enter First Number: "))
Second_Number = int(input("Enter Second Number: "))
Third_Number = int(input("Enter Third Number: "))

Largest_Number = Third_Number if Third_Number > First_Number else First_Number if First_Number > Second_Number else Second_Number
print(f"Maximum number out of given three numbers is: {Largest_Number}!")