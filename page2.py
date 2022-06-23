import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from helper_func import *
from helper_func_1 import *
import os
#from tkinter import *
from tkinter import ttk




def browsefunc(ent):
    filename = askopenfilename(filetypes=([
        ("image", ".jpeg"),
        ("image", ".png"),
        ("image", ".jpg"),
    ]))
    ent.insert(tk.END, filename)  # add this



def nav_to_checkout(window):
    checkout_frame(window)

def checkout_frame(destroy_this_win=None):
    if destroy_this_win is not None:
        destroy_this_win.destroy()

    root = tk.Tk()
    root.title("AUC Parking: Search ")
    root.geometry("500x500")  # 300x200
    # root.withdraw()
    root.call('wm', 'attributes', '.', '-topmost', True)
    uname_label = tk.Label(root, text="AUC Parking: Search", font=10)
    uname_label.place(x=90, y=100)

    profilepic_message = tk.Label(root, text="Number-Plate", font=10)
    profilepic_message.place(x=10, y=230)

    profilepic_entry = tk.Entry(root, font=10)
    profilepic_entry.place(x=150, y=230)

    profilepic_browse_button = tk.Button(
        root, text="Browse", font=10, command=lambda: browsefunc(profilepic_entry))
    profilepic_browse_button.place(x=400, y=190)

    facepic_browse_button = tk.Button(
        root, text="Capture", font=10, command=lambda: captureFace(profilepic_entry))
    facepic_browse_button.place(x=400, y=240)

    register_button = tk.Button(
        root, text="Search", font=10, command=lambda: checkout_clicked(window=root,
                                                                       pic_path=profilepic_entry.get()))

    register_button.place(x=200, y=320)

    root.mainloop()


checkout_frame()
