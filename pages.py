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


def nav_to_checkin(window):
    checkin_frame(window)

'''
def nav_to_checkout(window):
    checkout_frame(window)
'''

def checkin_frame(destroy_this_win=None):
    if destroy_this_win is not None:
        destroy_this_win.destroy()
    root = tk.Tk()
    root.title("AUC Parking: Checkin")
    root.geometry("400x500")  # 300x200
    # root.withdraw()
    root.call('wm', 'attributes', '.', '-topmost', True)

    uname_label = ttk.Label(root, text="AUC Parking:Checkin", font=10,)                                
    uname_label.place(x=140, y=50)

    entrytype_message = tk.Label(root, text="Entry Type: ", font=10)
    entrytype_message.place(x=10, y=120)
    
  
    # Create Combobox
    n = tk.StringVar() 
    car_typ = ttk.Combobox(root, width = 27, textvariable = n)
    car_typ.place(x=160, y=120) 
  
    # Adding combobox drop down list 
    car_typ['values'] = (' Faculty',  
                          ' Student', 
                          ' Visitor') 
                           
   
    car_typ.current()

    facepic_message = tk.Label(root, text="Vehicle Owner ", font=10)
    facepic_message.place(x=10, y=280)

    own_name = tk.Entry(root, font=10)
    own_name.place(x=160, y=280)

    #own_name.insert(tk.END,'')
    facepic_entry = tk.Entry(root, font=10)
    facepic_entry.place(x=160, y=170)

    np_message = tk.Label(root, text="Number-Plate ", font=10)
    np_message.place(x=10, y=170)


    facepic_browse_button = tk.Button(
        root, text="Capture", font=10, command=lambda: captureFace(facepic_entry))
    facepic_browse_button.place(x=160, y=230)

    profilepic_browse_button = tk.Button(
        root, text="Browse", font=10, command=lambda: browsefunc(facepic_entry))
    profilepic_browse_button.place(x=250, y=230)


    Purposes = tk.Label(root, text="Purpose of visit ", font=10)
    Purposes.place(x=10, y=320)

    Purposes = tk.Entry(root, font=10)
    Purposes.place(x=160, y=320)
    '''
    visit_message = tk.Label(root, text="Phone Number ", font=10)
    visit_message.place(x=10, y=360)

    visit_message = tk.Entry(root, font=10)
    visit_message.place(x=140, y=360)
    
    '''
    #USED TO ADD NEW ENTRIES TO DATABASE
    login_button = tk.Button(
        root, text="Submit", font=10, command=lambda: checkin_clicked(window=root, base_name=own_name.get(), pov=Purposes.get(), pic_path=facepic_entry.get()) )
                                                                        

    login_button.place(x=180, y=400)
    '''
    register_nav_button = tk.Button(
        root, text="Go to Checkout Page", font=10, command=lambda: nav_to_checkout(window=root,))

    register_nav_button.place(x=250, y=450) '''

    root.mainloop()

'''
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
                                                                       pic_path=profilepic_entry.get(),))

    register_button.place(x=200, y=320)

    root.mainloop()


checkout_frame()

'''
checkin_frame()
