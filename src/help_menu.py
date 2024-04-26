from tkinter import *
from tkinter.messagebox import *
import sys


class Help():

    def about(root):
        showinfo(title="About", message="Light is a fast and simple text editor implemented in python.")


def main(root, text, menubar):

    help = Help()

    helpMenu = Menu(menubar)
    helpMenu.add_command(label="About", command=help.about)
    menubar.add_cascade(label="Help", menu=helpMenu)

    root.config(menu=menubar)


if __name__ == "__main__":
    print("Please run 'main.py'")
