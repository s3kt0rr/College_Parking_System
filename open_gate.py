import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from helper_func import *
from helper_func_1 import *
import os
#from tkinter import *
from tkinter import ttk
#from pages import *



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
    root.title("AUC Parking: Open Gate ")
    root.geometry("500x500")  # 300x200
    # root.withdraw()
    root.call('wm', 'attributes', '.', '-topmost', True)
    uname_label = tk.Label(root, text="AUC Parking: Open Gate", font=10)
    uname_label.place(x=170, y=10)
    '''
    profilepic_message = tk.Label(root, text="Number-Plate", font=10)
    profilepic_message.place(x=10, y=230)

    profilepic_entry = tk.Entry(root, font=10)
    profilepic_entry.place(x=150, y=230)

    profilepic_browse_button = tk.Button(
        root, text="Browse", font=10, command=lambda: browsefunc(profilepic_entry))
    profilepic_browse_button.place(x=400, y=190)

    facepic_browse_button = tk.Button(
        root, text="Capture", font=10, command=lambda: captureFace(profilepic_entry))
    facepic_browse_button.place(x=400, y=240) '''

    register_button = tk.Button(
        root, text="OPEN GATE", font=20, command=lambda: open_th_gate()) 
    register_button.place(x=50, y=250)

    register_button2 = tk.Button(
        root, text="CLOSE GATE", font=20, command=lambda: close_th_gate()) 
    register_button2.place(x=250, y=250)

    def open_th_gate():
        messagebox.showinfo('information', 'Opening The Gate')

    def close_th_gate():
        messagebox.showinfo('information', 'Closing The Gate')


    root.mainloop()


checkout_frame()
