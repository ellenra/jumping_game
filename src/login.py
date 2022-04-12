from tkinter import *
from tkinter import constants
import tkinter as tk
import tkinter.font as font

window = Tk()
FONT = font.Font(family='DeJavu Sans')

def validate_login(username, password):
    print("username entered :", username.get())
    print("password entered :", password.get())
    return

def register():
    register_screen = Toplevel(window)
    register_screen.title("Register")
    register_screen.geometry("400x200")
    register_screen.configure(bg='#B0E0E6')
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Enter username and password", bg='#B0E0E6', font=FONT).pack()
    Label(register_screen, text="").pack()

    username_label = Label(register_screen, text="Username: ", bg='#B0E0E6')
    password_label = Label(register_screen, text="Password: ", bg='#B0E0E6')
    username_entry = Entry(register_screen, textvariable=username, bg='#7BD5D5')
    password_entry = Entry(register_screen, textvariable=password, bg='#7BD5D5')

    username_label.pack()
    username_entry.pack()
    password_label.pack()
    password_entry.pack()

    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg='#56BACE', font=FONT, command=window.destroy).pack()

