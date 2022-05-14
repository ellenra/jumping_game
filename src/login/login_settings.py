import sqlite3
from tkinter import Tk, font
import os

WINDOW = Tk()
FONT = font.Font(family='DeJavu Sans')
GEOMETRY = "400x200"
WINDOW.geometry(GEOMETRY)
WINDOW.title("Login")
WINDOW.configure(bg='#B0E0E6')

CONNECT = sqlite3.connect(os.path.join("login_information.db"))
CURSOR = CONNECT.cursor()

CURSOR.execute('''CREATE TABLE IF NOT EXISTS
               information(username TEXT, email TEXT, password TEXT)''')
CONNECT.commit()
