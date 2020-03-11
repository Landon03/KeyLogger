FirstName1 = input("What is your first name: ").upper()
LastName2 = input("What is your last name: ").upper()
class Person:
    def __init__(self):
        print("____Your-Name___")

    def FullName(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    def PrintFullname(self):
        print("Hi your name is, " + self.firstname, self.lastname)

personname = Person()
personname.FullName(FirstName1, LastName2)
personname.PrintFullname()