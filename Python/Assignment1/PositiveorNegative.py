# Positive, Negative, or Zero

Value = int(input("Enter a number to check whether it is Positive, Negative, or Zero: "))
if (Value == 0):
    print(f"Entered value is a Zero!")
elif (Value < 0):
    print(f"Entered value '{Value}' is a Negative number!")
else:
    print(f"Entered value '{Value}' is a Positive number!")