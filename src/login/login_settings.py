import sqlite3
from tkinter import Tk, font
import os

window = Tk()
FONT = font.Font(family='DeJavu Sans')
GEOMETRY = "400x200"
window.geometry(GEOMETRY)
window.title("Login")
window.configure(bg='#B0E0E6')

connect = sqlite3.connect(os.path.join("login_information.db"))
cursor = connect.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS
               information(username TEXT, email TEXT, password TEXT)''')
connect.commit()
