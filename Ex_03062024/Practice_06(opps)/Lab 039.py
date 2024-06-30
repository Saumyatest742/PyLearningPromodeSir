class Dog:
    name = None

    def sleep(self):
        print("Sleeping")


dog1=Dog()
print(dog1.name)
dog1.name = "Maltos"
print(dog1.name)
dog1.sleep()
print("*********")

dog2=Dog()
print(dog2.name)
dog2.name = "Maow"
print(dog2.name)
dog2.sleep()
print("*********")