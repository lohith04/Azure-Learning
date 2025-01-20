#Check Leap Year

Year = int(input("Enter a Year to check whether it is a leap year or not: "))
if(Year % 400 == 0 and Year % 100 == 0):
    print(f"Entered year '{Year}' is a Leap Year!")
elif(Year % 4 == 0 and Year % 100 != 0):
    print(f"Entered year '{Year}' is a Leap Year!")
else:
    print(f"Entered year '{Year}' is not a Leap Year!")