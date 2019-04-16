__author__ = 'DIPAL'
from tkinter import *

root = Tk()
lable_1 = Label(root, text="Name")
lable_2 = Label(root, text="Password")
entery1 = Entry(root)
entery2 = Entry(root)
lable_1.grid(row=0,sticky=W)
lable_2.grid(row=1,sticky=W)
entery1.grid(row=0, column=1)
entery2.grid(row=1, column=1)
c = Checkbutton(root, text="keep me login!")
c.grid(columnspan="3")
root.mainloop()