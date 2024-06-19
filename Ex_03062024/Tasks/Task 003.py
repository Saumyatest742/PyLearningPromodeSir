# LEAP YEAR
# Create a program to find given year is leap year
# A leap year is divisible by 4 but not by 100, except for years divisible by 400.
#Use if else to take the desission
# Year%4 = 0
year = int(input("Enter the year: \n"))
if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print("Leap Year")
        else:
            print("Not a Leap Year")
