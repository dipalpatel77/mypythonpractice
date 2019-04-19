__author__ = 'DIPAL'
from Tkinter import *
root=Tk()
one=Label(root,text="one",bg="red",fg="white")
one.pack()
two=Label(root,text="two",bg="green",fg="black")
two.pack(side=RIGHT,fill=X)
three=Label(root,text="three",bg="blue",fg="white")
three.pack(side=LEFT,fill=Y)
root.mainloop()