#Grade Calculator

Marks = int(input("Enter Marks of Student: "))
if Marks < 0 or Marks > 100 :
    print("Enter Marks in only Range of 0 to 100")
else:
    if Marks >= 90 and Marks <= 100:
        Grade = "A"
    elif Marks >= 80 and Marks <= 89:
        Grade = "B"
    elif Marks >= 70 and Marks <= 79:
        Grade = "C"
    elif Marks >= 60 and Marks <= 69:
        Grade = "D"
    else:
        Grade = "F"
    print(f"Student got a Grade of: {Grade}")