from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.tile('Dropdown Menu')
#root.iconbitmap('C/:your icon path here')
root.geometry("400x400")

# Dropdown Boxes

clicked = StringVar()

drop  = OptionMenu(root,clicked, "Monday","Tuesday","Wednesday","Thussday","Friday")
drop.pack()






root.mainloop()
