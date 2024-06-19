# Multiple condition
# Match case
number =  int(input("Enter the number: "))
match number:
    case 1:
        print("number is 1")
    case 2:
        print("number is 2")
    case 3:
        print("number is 3")
    case 4:
        print("number is 4")
    case 5:
        print("number is 5")
    case _:
        print("No idea")