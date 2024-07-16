class VWOlogin:
    def __init__(self, email, password):
        self.__email = None
        self.__password = None
        self__email = email
        self__password = password

    def login_confirm(self):
        if self.__email == "abc@gmail.com" and self.__password == "123":
            print("Login successful")
        else:

            print("Not allowed")


# This is end of class

page1 = VWOlogin("abc@gmail.com", "123")
page1.login_confirm()
