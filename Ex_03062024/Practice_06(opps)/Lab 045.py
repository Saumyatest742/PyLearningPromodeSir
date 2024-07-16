class Car:

    def __init__(self):
        self.public_variable = "public"
        self._protected_variable = "protected"
        self.__private_variable = "private"

    def __private_method(self):
        print("Private method called")

    def printname(self):
        print("I am allowed public")


# End of class

alto = Car()
alto.printname()
