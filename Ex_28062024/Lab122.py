class VWOLoginPage:
    email = None
    password = None

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def login_confirm(self):
        if self.email == "pramod@gmail.com" and self.password == "Pass123":
            print("Allowed to enter")
        else:
            print("Not allowed")

# This is the end of the class
email = input("Enter the email\n")
password = input("Enter the password\n")
amit = VWOLoginPage(email, password)
amit.login_confirm()
#
# pramod = VWOLoginPage("pramod@gmail.com", "Pass123")
# pramod.login_confirm()