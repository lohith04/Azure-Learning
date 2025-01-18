#Number in Range

LowerBound = int(input("Enter the LowerLimit of the Range: "))
UpperBound = int(input("Enter the UpperLimit of the Range: "))
Number = int(input("Enter a number to check whether number is in Range or not: "))
if Number <= UpperBound and Number >= LowerBound:
    print(f"Entered number '{Number}' is In Range")
else:
    print(f"Entered number '{Number}' is Out of Range")