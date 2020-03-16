"""
Heads or Tails by computer
https://www.facebook.com/landon.jacobs.735?ref=bookmarks

"""
from tkinter import *
import random
root = Tk()
root.geometry("1280x1080")
root.configure(background="lightblue")
root.title("Heads or tails by Landon Jacobs")
value = (random.randint(1, 2))
if value==1:
    photo1 = PhotoImage(file="heads.png")
    label1 = Label(root, image=photo1)
    label1.pack()

    
if value==2:
    photo2 = PhotoImage(file="tails.png")
    label2 = Label(root, image=photo2)
    label2.pack()

root.mainloop()