write a program to find a grade after taking marks from the user input
# Grading scale -
#If marks above 90 - A grade
#If  marks between 80 to 90 - B grade
#If marks between 70 to 80 - C grade
#If marks below 70 - D grade
#If marks below 60 - Fail
# If marks above 100 or below 0 - Invalid marks

# Take input from the user

marks = int(input("Enter your marks: "))
#out put = A,B,C,D,Fail,Invalid - String
#marks >= 90 and <= 100 - A grade
#marks >= 80 and <= 89 - B grade
#marks >= 70 and <= 79 - C grade
#marks >= 60 and <= 69 - D grade
#marks >= 0 and <= 59 - Fail
#marks > 100 or <= 0 - Invalid marks

if marks >= 90 and marks <= 100:
    print("A grade")
elif marks >= 80 and marks <= 89:
    print("B grade")

elif marks >= 70 and marks <= 79:
    print("C grade")

elif marks >= 60 and marks <= 69:
    print("D grade")

elif marks >= 0 and marks <= 59:
    print("Fail")

else:
    print("Invalid marks")

