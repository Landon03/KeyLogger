"""

https://github.com/Landon03/Python_Scripts

"""


import os
FirstName1 = input("What is your first name: ").upper()
LastName2 = input("What is your last name: ").upper()
class Person:
    def __init__(self):
        print("Name Printer by Landon Jacobs")

    def FullName(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    def PrintFullname(self):
        print("Hi your name is, " + self.firstname, self.lastname)

personname = Person()
personname.FullName(FirstName1, LastName2)
personname.PrintFullname()
os.system("pause")
os.system("exit")
