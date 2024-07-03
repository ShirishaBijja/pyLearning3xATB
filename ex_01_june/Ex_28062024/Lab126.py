class VWOLogin:

    def __init__(self, email, password):
        self.__email = email
        self.__password = password

    def login_confirm(self):
       if self.__email == "abc@email.com" and self.password == "123":
           print("Allowed")
       else:
           print("Not allowed")


page1 = VWOLogin("abc@gmail.com", "123")
print(page1.email)