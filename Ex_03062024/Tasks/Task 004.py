#Triangle Classifier
#Write a program that clisifies  a triangle based on the lengths of its 3 sides.
#The program should prompt the user to input the lengths of the three sides of the triangle.
#Then, it should determine the type of triangle based on the lengths of its sides.
#For example, if all three sides are equal, the triangle is an equilateral triangle.
#If the two sides of the triangle are equal, the triangle is an isosceles triangle.
#If none of the sides are equal, the triangle is a scalene triangle.
#USe if else statement - if

#Prompt the user to input the lengths of the three sides of the triangle
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))
if side1 == side2 and side2 == side3:
    print("The triangle is an Equilateral triangle.")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("The triangle is an Isosceles triangle.")

else:
    print("The triangle is a Scalene triangle.")
