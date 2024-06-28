# Web Automation - Selenium
# Page - You are going to automate

class VWOLoginPage:
    email = None
    password = None

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def login_confirm(self):
        if self.password == "Pass123":
            print("Allowed to enter")
        else:
            print("Not allowed")

# This is the end of the class
amit = VWOLoginPage("amit@gmail.com", "124")
amit.login_confirm()

pramod = VWOLoginPage("pramod@gmail.com", "Pass123")
pramod.login_confirm()


