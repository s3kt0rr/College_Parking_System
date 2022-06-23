from tkinter import ttk
from datetime import datetime
from sqlite3.dbapi2 import Cursor, Timestamp
from helper_func import *
from db_queries import *

import tkinter as tk

import sqlite3


def connect():

    con1 = sqlite3.connect('vehicles.db')

    cur1 = con1.cursor()

    cur1.execute("CREATE TABLE IF NOT EXISTS vehicle(id INTEGER PRIMARY KEY, First TEXT, Surname TEXT)")

    con1.commit()

    con1.close()

def View():

    conn = sqlite3.connect('vehicles.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM vehicle")
    rows = cur.fetchall()    

    for row in rows:

        print(row) 

        tree.insert("", tk.END, values=row)        

    con1.close()


# connect to the database

connect() 

root = tk.Tk()

tree = ttk.Treeview(root, column=("c1", "c2", "c3","c4","c5"), show='headings')

tree.column("#1", anchor=tk.CENTER)

tree.heading("#1", text="Number Plate")

tree.column("#2", anchor=tk.CENTER)

tree.heading("#2", text="In Time")

tree.column("#3", anchor=tk.CENTER)

tree.heading("#3", text="Out Time")
tree.column("#3", anchor=tk.CENTER)

tree.heading("#4", text="Owner Name")
tree.column("#4", anchor=tk.CENTER)

tree.heading("#5", text="Purpose")
tree.column("#5", anchor=tk.CENTER)

'''
tree.heading("#6", text="Phone Number")
tree.column("#6", anchor=tk.CENTER)

tree.heading("#7", text="Type")
tree.column("#7", anchor=tk.CENTER)
'''
tree.pack()

button1 = tk.Button(text="Display data", command=View)

button1.pack(pady=10)



root.mainloop()