class person :
    #Atributos
    name = None
    id = None
    age = None
    phone_number = None

    #Behavior
    def walk(self):
        print("I'm walking")
    def run(self):
        print("I'm running")
    def sleep(self):
        print("I'm sleeping")

#____End of the class____

#Creating an object of the class
saumya = person()
saumya.name = "Saumya ranjan"
saumya.age = 10

punam = person()
punam.name = "Punam P"