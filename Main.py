# username and password authentication by Landon Jacobs
# https://www.facebook.com/landon.jacobs.735?ref=bookmarks
import os

createuser = input("choose a username: ")
createpassword = input("choose a password: ")
os.system("cls")
Usernamelen = len(createuser)
Passwordlen = len(createpassword)

def recognition():
    username = input("Username: ")
    Password = input("Password: ")
    if username==createuser and Password==createpassword:
        print("correct Username and Password")
        os.system("pause")
    else:
        print("incorrect Username or password")
        os.system("pause")

def length():
    if Usernamelen and Passwordlen < 5:
        print("Username and Password must be more than 5 characters")
        os.system("pause")
        os.system("cls")
        os.system("exit")
    if Usernamelen and Passwordlen > 5:
        recognition()
length()

