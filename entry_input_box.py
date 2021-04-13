from tkinter import *

root = Tk()

e = Entry(root, width = 40, border = 10)
e.pack()
# Get user input
e.get()
e.insert(0, "Enter your Name:")

def myClick():
    myLabel = Label(root, text=e.get())
    myLabel.pack()

    
myButton = Button(root, text="Enter Your Name", padx=50, pady=50, command=myClick,)
myButton.pack()
# myButton.grid(row=0, column = 0)

root.mainloop()
