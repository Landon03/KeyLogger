import os

class name:

	def __init__(self, firstname, lastname):

		self.firstname = firstname
		self.lastname = lastname

	def printname(self):
		print("hello,", self.firstname, self.lastname)

name = name("Landon", "Jacobs")
name.printname()
os.system("pause")