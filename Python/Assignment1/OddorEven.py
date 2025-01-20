#Odd or Even

Value = int(input("Enter a number to check whether Even or Odd: "))
if(Value <= 0):
    print("Enter a valid number!")
else:     
    if (Value % 2 == 0):
        print(f"Entered values '{Value}' is an Even number!")
    else:
        print(f"Entered value '{Value}' is an Odd number!")