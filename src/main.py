# import required sub-systems
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.font import Font
from tkinter.scrolledtext import *

# import local file
import file_menu
import edit_menu
import format_menu
import help_menu

root = Tk()

root.title("Light")
root.geometry("640x480") #Default resolution
root.minsize(width=400, height=400) # user can resize the window but won't be able to shrink it smaller than 400px

text = ScrolledText(root, state='normal', height=400, width=400, wrap='word', pady=2, padx=3, undo=True)
text.pack(fill=Y, expand=1)
text.focus_set()

menubar = Menu(root)

file_menu.main(root, text, menubar)
edit_menu.main(root, text, menubar)
format_menu.main(root, text, menubar)
help_menu.main(root, text, menubar)

#main program loop
root.mainloop()
