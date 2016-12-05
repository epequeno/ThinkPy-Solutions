# Write a program that creates a GUI with a single button. When the button is
# pressed it should create a second button. When that button is pressed, it
# should create a label that says, "Nice job!".
# What happens if you press the buttons more than once? You can see my 
# solution at thinkpython.com/code/button_demo.py

# Current Status: Complete
#note: Written in Python 3.5
#Author: bknox95

from tkinter import messagebox
import tkinter as tk
class Window1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text = 'Press Me', width = 25, command = self.new_window)
        self.button1.pack()
        self.frame.pack()
    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Window2(self.newWindow)


 #Creates Window2 with button2 that displays a "Nice Job" message
class Window2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button2 = tk.Button(self.frame, text = 'Now Press Me', width = 25, command = self.new_window)
        self.button2.pack()
        self.frame.pack()
    def new_window(self):
        msg=messagebox.showinfo(message="Nice Job!")
        self.master.destroy()


def main():
    root = tk.Tk()
    app = Window1(root)
    root.mainloop()

if __name__ == '__main__':
    main()
