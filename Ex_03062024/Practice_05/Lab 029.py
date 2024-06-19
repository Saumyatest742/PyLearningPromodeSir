def classroom(name,password):
    if name == "Saumya":
        if password == "123":
            print("Your are allowed in to the class")
        else:
            print("You are not allowed")

classroom("Saumya", "123")
classroom("Punam", "123")
classroom("Saumya", "1234")