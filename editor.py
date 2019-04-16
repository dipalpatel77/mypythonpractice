#from tkFileDialog import asksaveasfilename, asksaveasfile
# "#" is used to comment the line
__author__ = 'DIPAL'
# tkinter is the library contains the classes and function for gui designing
from Tkinter import *
import tkFileDialog
from tkMessageBox import *  # the functions of displaying messagebox such as showerror
filename = None

def donothing():
  print("successfully run")

def newFile(): #creates new file
  global filename
  filename = "untitled"
  text.delete(0.0, END)


def saveFile():
  global filename
  bx = str(text.get(0.0, END))
  f = tkFileDialog.asksaveasfile(mode='w',defaultextension=".txt") # function from tkinter.filedialog
  f.write(bx)
  f.close()


def saveAs():
  # f = asksaveasfile(mode='r', defaultextension='.txt')
  f = tkFileDialog.asksaveasfile(mode='w',defaultextension=".txt")  # function from tkinter.filedialog
  t = text.get(0.0, END)
  try:
    f.write(t.rstrip())
  except:
    showerror(title="oops!", message="unable to open")


def openfile():
  f = tkFileDialog.askopenfile(mode='r')
  t = f.read()
  text.delete(0.0, END)
  text.insert(0.0, t)

def copy():
  self.clipboard_clear()
  text = self.get("sel.first", "sel.last")
  self.clipboard_append(text)

def cut():
  self.copy()
  self.delete("sel.first", "sel.last")

def paste():
  text = self.selection_get(selection='CLIPBOARD')
  self.insert('insert', text)

tk = Tk()  # from tkinter
tk.title("MY EDITOR")
tk.minsize(width=400, height=400)
tk.maxsize(width=700, height=700)

text = Text(tk, width=400, height=400)
text.pack()
ax= Menu(tk)
menubar = Menu(tk)  # menu is predefined inbuilt class from tkinter
filemenu = Menu(menubar)
editmanu=Menu(ax)
# functions from class menu
filemenu.add_command(label="newFile", command=newFile)
filemenu.add_command(label="openfile", command=openfile)
filemenu.add_command(label="save", command=saveFile)
filemenu.add_command(label="saveas", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="quit", command=tk.quit)
editmanu.add_command(label="cut", command=cut)
editmanu.add_command(label="paste", command=paste)
editmanu.add_command(label="copy",command=donothing)
ax.add_cascade(label="edit", menu=editmanu)
menubar.add_cascade(label="File", menu=filemenu)
tk.config(menu=menubar)
tk.config(menu=ax)
tk.mainloop()