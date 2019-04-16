from tkinter import *

# Define
def New():
   print("New")

def Open():
   OpenFile = filedialog.askopenfilename( filetypes = ( ("ztext file", "*.z"),("zytext", "*.zy") ) )
   print(OpenFile)

def make_menu(w):
    global the_menu
    the_menu = Menu(w, tearoff=0)
    the_menu.add_command(label="Cut")
    the_menu.add_command(label="Copy")
    the_menu.add_command(label="Paste")

def show_menu(e):
    w = e.widget
    the_menu.entryconfigure("Cut", command=lambda: w.event_generate("<<Cut>>"))
    the_menu.entryconfigure("Copy", command=lambda: w.event_generate("<<Copy>>"))
    the_menu.entryconfigure("Paste", command=lambda: w.event_generate("<<Paste>>"))
    the_menu.tk.call("tk_popup", the_menu, e.x_root, e.y_root)

def Save():
    print("Save")

def Save_as():
    SaveFile = filedialog.asksaveasfilename( filetypes = ( ("ztext file", "*.z"),("zytext",         "*.zy") ) )
    print(SaveFile)

def Close():
    print("Close")

def Exit():
    root.destroy

def Undo():
    print("Undo")

def Select_All():
    print("Select_All")

def Help_Index():
    print("Help Index")

def About():
    #About window
    top = Toplevel()
    top.title("About...")

    msg = Message(top, text="Note pad")
    msg.pack()

    top.mainloop()


#root window
root = Tk()
root.title("Note")
make_menu(root)

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

textbox = Text(root, yscrollcommand=scrollbar.set)
textbox.pack(side=LEFT, fill=BOTH)

textbox.bind_class("Text", "<Button-3><ButtonRelease-3>", show_menu)

#Menu Bar
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=New)
filemenu.add_command(label="Open", command=Open)
filemenu.add_command(label="Save", command=Save)
filemenu.add_command(label="Save as...", command=Save_as)
filemenu.add_command(label="Close", command=Close)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=Undo)
editmenu.add_separator()
editmenu.add_command(label="Cut", command=lambda: w.event_generate("<<Cut>>"))
editmenu.add_command(label="Copy", command=lambda: w.event_generate("<<Copy>>"))
editmenu.add_command(label="Paste", command=lambda: w.event_generate("<<Paste>>"))
editmenu.add_command(label="Select All", command=Select_All)
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=Help_Index)
helpmenu.add_command(label="About...", command=About)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

root.mainloop()