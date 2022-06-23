import tkinter as tk
import tkinter.font as font
from PIL import Image, ImageTk
import os
import sys
import subprocess

from helper_func import *
from helper_func_1 import * 
#from pages import *


window = tk.Tk()
window.title("AUC_PARKING")
window.iconphoto(True, tk.PhotoImage(file='cr_logo.png'))
window.geometry('800x400')
window.configure(bg='slategray2')


frame1 = tk.Frame(window, bg='slategray2')

icon = Image.open('icons/auclogo.png')
icon = icon.resize((250,85), Image.Resampling.LANCZOS)
icon = ImageTk.PhotoImage(icon)
label_icon = tk.Label(frame1, image=icon, bg='slategray2')
label_icon.grid(row=1, pady=(10,10), column=1)

#label_title = tk.Label(frame1, text="AUC Parking Management", width=20, fg='gray1', bg='slategray2',font = ("Times New Roman", 15)).grid(padx = 100 , pady= 0)
#label_font = font.Font(size=10, weight='bold',family='Times New Roman').grid(row = 0, column = 1)
#label_title['font'] = label_font
#font = ("Times New Roman", 15)).grid(row = 0, column = 1)
#label_title.grid(padx=60, pady=(10,10))


btn1_image = Image.open('icons/Register.png')
btn1_image = btn1_image.resize((50,50), Image.Resampling.LANCZOS )
btn1_image = ImageTk.PhotoImage(btn1_image)

btn2_image = Image.open('icons/search.png')
btn2_image = btn2_image.resize((50,50), Image.Resampling.LANCZOS)
btn2_image = ImageTk.PhotoImage(btn2_image)

btn5_image = Image.open('icons/exit.png')
btn5_image = btn5_image.resize((50,50), Image.Resampling.LANCZOS)
btn5_image = ImageTk.PhotoImage(btn5_image)

btn3_image = Image.open('icons/access.png')
btn3_image = btn3_image.resize((50,50), Image.Resampling.LANCZOS)
btn3_image = ImageTk.PhotoImage(btn3_image)

btn6_image = Image.open('icons/dbms.png')
btn6_image = btn6_image.resize((50,50), Image.Resampling.LANCZOS)
btn6_image = ImageTk.PhotoImage(btn6_image)
# --------------- Button -------------------#
btn_font = font.Font(size=15)

def run_program():
    subprocess.call(["python", "pages.py"])

btn1 = tk.Button(frame1, text=' Register', height=90, width=170, fg='white', bg='grey31', command = run_program, compound = 'top', image=btn1_image)
btn1['font'] = btn_font
btn1.grid(row=3, pady=(10,5))


def run_program2():
    subprocess.call(["python", "page2.py"])

btn2 = tk.Button(frame1, text=' Search', height=90, width=170, fg='white', bg='grey31', command=run_program2, compound='top', image=btn2_image)
btn2['font'] = btn_font
btn2.grid(row=3, pady=(10,5), column=1, padx=(10,5))



btn5 = tk.Button(frame1,text='Exit', height=90, width=170, fg='white', bg='grey31', command=window.quit, compound='top', image=btn5_image)
btn5['font'] = btn_font
btn5.grid(row=5, column=1, pady=(20,15))

def run_program3():
    subprocess.call(["python", "open_gate.py"])

#btn_font = font.Font(size=20)
btn3 = tk.Button(frame1, text='Open', height=90, width=170, fg='white', bg='grey31', command= run_program3, image=btn3_image, compound='top')
btn3['font'] = btn_font
btn3.grid(row=3,column=3, pady=(10,5))

def run_program4():
    subprocess.call(["python", "sql_show.py"])

btn6 = tk.Button(frame1,text='Database', height=90, width=170, fg='white', bg='grey31', command=run_program4, compound='top', image=btn6_image)
btn6['font'] = btn_font
btn6.grid(row=5, pady=(10,5), padx=(10,5))


frame1.pack()
window.mainloop()
