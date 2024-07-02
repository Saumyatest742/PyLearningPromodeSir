class Car:

    def __init__(self):
        self.public_variable = "public"
        self._protected_variable = "protected"
        self.__private_variable = "private"


# End of class

alto = Car()
alto.public_variable = "Hahaha"
