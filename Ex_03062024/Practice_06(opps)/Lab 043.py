# Web automation with Selenium
# Page - You are going to automate

class VWOlogin_page:
    email = None
    password = None

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def login_confirm(self):
        if self.password == "pass123":
            print("Login successful")
        else:
            print("Login failed")


# This is end of Class

saumyaranjan = VWOlogin_page("saumya@example.com", "123")
saumyaranjan.login_confirm()
ramNath = VWOlogin_page("ram@example.com", "pass123")
ramNath.login_confirm()
