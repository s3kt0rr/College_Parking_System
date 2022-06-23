import sqlite3
from datetime import datetime
from sqlite3.dbapi2 import Cursor, Timestamp
from helper_func import *
from helper_func_1 import *
#from pages import pov

def addVehicleCheckin(vehicle_num, base_name,pov):
    conn = sqlite3.connect('vehicles.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS vehicle(
        vehicle_num text PRIMARY KEY,
        intime timestamp,
        outtime timestamp,
        base_name varchar,
        pov varchar
        );''')
    conn.commit()
    conn.execute("INSERT OR REPLACE INTO vehicle (vehicle_num,intime,own_name, Purpose) \
        VALUES (?,?,?,?)", (vehicle_num, datetime.now(), base_name, pov))
    conn.commit()
    conn.close()
    return True


def getIntime(vehicle_num):
    conn = sqlite3.connect('vehicles.db')
    cur = conn.cursor()
    cur.execute("SELECT intime FROM vehicle WHERE vehicle_num=?",
                (vehicle_num,))

    rows = cur.fetchall()
    conn.close()
    return rows[0]


def view_db():
    conn = sqlite3.connect('vehicles.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM vehicle ")
    rows = cur.fetchall()
    print(rows)
    conn.close()


def addVehicleCheckout(vehicle_num):
    conn = sqlite3.connect('vehicles.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS vehicle(
        vehicle_num text PRIMARY KEY,
        intime timestamp,
        outtime timestamp,
        own_name text,
        Purpose text
       

        );''')
    conn.commit()
    end_time = datetime.now()
    #st = getIntime(vehicle_num)
    #start_time = datetime.fromisoformat(st)
    outtime = end_time
    conn.execute("UPDATE vehicle SET outtime = ?   WHERE vehicle_num = ?",
                 (outtime, vehicle_num))
    conn.commit()
    conn.close()
    return True


def getCheckoutdetails(vehicle_num):
    conn = sqlite3.connect('vehicles.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM vehicle WHERE vehicle_num=?", (vehicle_num,))
    rows = cur.fetchall()
    conn.close()
    return rows[0]



# addVehicleCheckin('Mh12345', 12.5165)
# addVehicleCheckout('Mh12345')
# view_db()
# addVehicleCheckin('AIBACC', 163.6516)
# addVehicleCheckout('AIBACC')
# view_db()

# addVehicleCheckin('JNOSCUOWV', 452.65)
# addVehicleCheckout('JNOSCUOWV')
# view_db()

# addVehicleCheckin('OJCNIIEC', 10.5165)
# addVehicleCheckout('OJCNIIEC')
# view_db()
# print(getCheckoutdetails('OJCNIIEC'))
