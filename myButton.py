from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look! I Clicked a Button!!")
    myLabel.pack()

    
myButton = Button(root, text="Click Me!", padx=50, pady=50, command=myClick,)
myButton.pack()
# myButton.grid(row=0, column = 0)

root.mainloop()
