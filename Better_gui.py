from tkinter import *

root = Tk()

# Creating a Lebel widget
myLabel1 = Label(root, text="Hello World!").grid(row = 0, column=0)
myLabel2 = Label(root, text="My name is Ian Hudson").grid(row = 1, column=5)
myLabel3 = Label(root, text="                     ").grid(row = 1, column=1)
# Putting label widget onto the screen

#myLabel1.grid(row = 0, column=0)
#myLabel2.grid(row = 1, column=5)
#myLabel3.grid(row = 1, column=1)
root.mainloop()

