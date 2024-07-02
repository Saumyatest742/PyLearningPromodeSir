#Encapsulation-

# Bind the data variable with methods

class car:
    name = None
    password = 123

    def __init__(self):
        print("I am called when object is created")

    def change_password(self):
        self.password = 345

    #end of class


xuv = car
xuv.password = 345


