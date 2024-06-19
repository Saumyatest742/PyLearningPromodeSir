# Find the max between 3 numbers
# num1, num2, numb3
# num1> num2 and num1> num3 -- num1 is max
# num2 > num1 and num2 > num3 -- num2 is max
#
#
#
num1= int(input("Enter the 1st number: "))
num2= int(input("Enter the 2nd number: "))
num3= int(input("Enter the 3rd number: "))
if num1>num2 and num1>num3:
    print(num1)

elif num2>num1 and num2>num3:
    print(num2)

else:
    print(num3)

num4= int(input("Enter the 4th number: "))
num5= int(input("Enter the 5th number: "))
print(max(num4, num5))

