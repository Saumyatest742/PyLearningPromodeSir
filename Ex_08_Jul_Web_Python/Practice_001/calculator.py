
num1 = int(input("Enter your 1st number - "))
num2 = int(input("Enter your 2nd number - "))
operator = input("Enter your operator (+, - ,* , /, % - ")

if operator == '+' :
    print(num1+ num2)

elif operator == '-' :
    print(num1 - num2)
elif operator == '*' :
    print(num1* num2)
elif operator == '/' :
    print(num1/num2)
elif operator == '%' :
    print(num1%num2)

else:
    print("Invalid operation")
