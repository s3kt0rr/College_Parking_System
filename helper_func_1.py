from re import L
from helper_func import *
from db_queries import *
import tkinter as tk
from tkinter import messagebox


def checkin_clicked(window, base_name, pic_path, pov):
    new_pic_path = pic_path.replace('/', '\\')
    base_name = str(base_name)
    pov = str(pov)
    number_plate_str = getNumberPlateSting(new_pic_path)
    res = addVehicleCheckin(vehicle_num=number_plate_str, base_name=base_name,pov=pov)
    if(res == True):
        messagebox.showinfo(
            'SUCCESS!!!', 'Vehicle Info added To DB')


def checkout_clicked(window, pic_path):
    new_pic_path = pic_path.replace('/', '\\')
    number_plate_str = getNumberPlateSting(pic_path)
    res = addVehicleCheckout(vehicle_num=number_plate_str)
    ans = getCheckoutdetails(vehicle_num=number_plate_str)

    text_str = 'Number= '+str(ans[0])+'\n'+'Check-In Time= ' + str(ans[1])+'\n'+'Check-Out Time= '+str(ans[2])+'\n'+'Name Of Owner = '+str(ans[3])+'\n'+'Purpose = '+str(ans[4])+'\n'
    if(res == True): 
        messagebox.showinfo(
            'Vehicle Details', text_str)   
    # pass
