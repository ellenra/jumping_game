from tkinter import messagebox, Label, Entry, Button, StringVar, constants, Toplevel, Tk, font
import tkinter as tk
import sqlite3
import os

window = Tk()
FONT = font.Font(family='DeJavu Sans')
window.geometry("400x200")
window.title("Login")
window.configure(bg='#B0E0E6')

connect = sqlite3.connect(os.path.join("login_information.db"))
cursor = connect.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS
               information(username TEXT, email TEXT, password TEXT)''')
connect.commit()


def login():
    cursor.execute('''SELECT username, password FROM information
                   WHERE username=? AND password=?''', (username_verification.get(), 
                   password_verification.get()))
    row = cursor.fetchone()
    if row:
        window.destroy()
    else:
        error()


def register():
    register = Toplevel(window)
    global USERNAME, PASSWORD, EMAIL

    register.title("Register")
    register.geometry("300x200")
    register.configure(bg='#B0E0E6')

    USERNAME = StringVar()
    PASSWORD = StringVar()
    EMAIL = StringVar()

    label = Label(register, text="Enter information", bg='#B0E0E6', font=FONT)

    username_label = Label(register, text="Username: ", bg='#B0E0E6')
    email_label = Label(register, text="Email: ", bg='#B0E0E6')
    password_label = Label(register, text="Password: ", bg='#B0E0E6')

    username_entry = Entry(register, textvariable=USERNAME, bg='#7BD5D5')
    email_entry = Entry(register, textvariable=EMAIL, bg='#7BD5D5')
    password_entry = Entry(register, textvariable=PASSWORD, bg='#7BD5D5')

    button = Button(register, text="Register", width=10, height=1, bg='#56BACE',
                    font=FONT, command=add_to_database)

    label.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
    username_label.grid(padx=5, pady=5)
    username_entry.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

    email_label.grid(padx=5, pady=5)
    email_entry.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

    password_label.grid(padx=5, pady=5)
    password_entry.grid(row=3, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

    button.grid(columnspan=2, sticky=(constants.E,constants.W), padx=5, pady=5)




def add_to_database():
    global USERNAME, EMAIL, PASSWORD
    cursor.execute("INSERT INTO information VALUES (:username, :email, :password)", {
            'username': USERNAME.get(),
            'email': EMAIL.get(),
            'password': PASSWORD.get()
            })
    connect.commit()
    window.destroy()


def error():
    messagebox.showerror("Error", "Invalid username or password")

class LogInView:
    def __init__(self, root):
        self._root = root
        self._frame = tk.Frame(master=self._root)

    def start(self):
        global username_verification, password_verification
        heading = tk.Label(master=self._root, text="Login or Register", bg="#B0E0E6", font=FONT)
        username_verification = StringVar()
        password_verification = StringVar()

        username = tk.Label(master=self._root, text="Username", bg='#B0E0E6')
        username_entry = tk.Entry(master=self._root, bg ='#7BD5D5',
                                  textvariable=username_verification)
        password = tk.Label(master=self._root, text="Password", bg='#B0E0E6')
        password_entry = tk.Entry(master=self._root, bg='#7BD5D5',
                                  textvariable=password_verification)

        button = tk.Button(master=self._root, text="Start game", bg='#56BACE',
                           command=login, font=FONT)
        register_button = tk.Button(master=self._root, text="Register", bg="#56BACE",
                                    command=register, font=FONT)

        heading.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        username.grid(padx=5, pady=5)
        username_entry.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        password.grid(padx=5, pady=5)
        password_entry.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        button.grid(columnspan=2, sticky=(constants.E,constants.W), padx=5, pady=5)
        register_button.grid(columnspan=3, sticky=(constants.E,constants.W), padx=5, pady=5)

        self._root.grid_columnconfigure(1, weight=1, minsize=200)


ui = LogInView(window)
ui.start()

window.mainloop()
connect.close()

