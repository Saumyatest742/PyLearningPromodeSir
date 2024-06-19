def classroom(name):
    match name:
        case "Punam":
            print("Punam is allowed")
        case "Millan":
            print("Millan is allowed")
        case "Mikili":
            print("Mikili is allowed")
        case "Darshan":
            print("Darshan is allowed")
        case _:
            print("You are not allowed")

classroom("Punam")
classroom("Ravi")
classroom("Mikili")
classroom("Darshan")
classroom("Millan")
classroom("Saumya")
