from tkinter import *
import tkinter
import tkinter.messagebox
import sys
import os
import configparser


config = configparser.ConfigParser()
config.read("config.ini")
path1 = config.get("paths", "path1")
path2 = config.get("paths", "path2")
path3 = config.get("paths", "path3")
path4 = config.get("paths", "path4")
bl1 = config.get("button_labels", "bl1")
bl2 = config.get("button_labels", "bl2")
bl3 = config.get("button_labels", "bl3")
bl4 = config.get("button_labels", "bl4")
tl1 = config.get("title", "tl1")

root = Tk()
root.title('')
root.geometry('190x230')
root.resizable(width=False, height=False)




def fun(arg):
    if arg == 1:
        os.startfile(path1)
        root.destroy()
    elif arg == 2:
        os.startfile(path2)
        root.destroy()
    elif arg == 3:
        os.startfile(path3)
        root.destroy()
    elif arg == 4:
         os.startfile(path4)
         root.destroy()
""" elif arg == 5:
         #os.startfile(filepath5)
        tkinter.messagebox.showinfo("button 5", "button 5 used")
        root.destroy()
"""

l1 = Label(root, text=tl1).place(x = 38, y = 200)
b1 = Button(root, text=bl1, height=2, width=20, command=lambda: fun(1)).pack(pady=5)
b2 = Button(root, text=bl2, height=2, width=20, command=lambda: fun(2)).pack(pady=5)
b3 = Button(root, text=bl3, height=2, width=20, command=lambda: fun(3)).pack(pady=5)
b4 = Button(root, text=bl4, height=2, width=20, command=lambda: fun(4)).pack(pady=5)
#b5 = Button(root, text="Button 5", height=2, width=20,  command=lambda: fun(5)).pack()

root.mainloop()




