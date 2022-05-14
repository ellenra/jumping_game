from tkinter import messagebox, StringVar, constants
import tkinter as tk
from login.register_screen import CURSOR, WINDOW, CONNECT, FONT, register

USERNAME_VERIFICATION = 1
PASSWORD_VERIFICATION = 1

class LogInView:
    """Luokka, joka luo ja on vastuussa kirjautumisikkunanäkymästä.
    """
    def __init__(self, root):
        """Luo ikkunan juuret.

        Args:
            root: Ikkunan juuret, johon kaikki muut luodaan.
        """
        self._root = root
        self._frame = tk.Frame(master=self._root)

    def start(self):
        """Funktio, joka on hallinnassa kirjautumisikkunasta.
        """
        global USERNAME_VERIFICATION, PASSWORD_VERIFICATION

        heading = tk.Label(master=self._root, text="Login or Register", bg="#B0E0E6", font=FONT)
        USERNAME_VERIFICATION = StringVar()
        PASSWORD_VERIFICATION = StringVar()

        username = tk.Label(master=self._root, text="Username", bg='#B0E0E6')
        username_entry = tk.Entry(master=self._root, bg='#7BD5D5',
                                  textvariable=USERNAME_VERIFICATION)
        password = tk.Label(master=self._root, text="Password", bg='#B0E0E6')
        password_entry = tk.Entry(master=self._root, bg='#7BD5D5',
                                  textvariable=PASSWORD_VERIFICATION)

        button = tk.Button(master=self._root, text="Start game", bg='#56BACE',
                           command=login, font=FONT)
        register_button = tk.Button(master=self._root, text="Register", bg="#56BACE",
                                    command=register, font=FONT)

        heading.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        username.grid(padx=5, pady=5)
        username_entry.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        password.grid(padx=5, pady=5)
        password_entry.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        button.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        register_button.grid(columnspan=3, sticky=(constants.E, constants.W), padx=5, pady=5)

        self._root.grid_columnconfigure(1, weight=1, minsize=200)

def login():
    """Tarkastaa onko kirjautumistiedot tietokannassa.
    """
    CURSOR.execute('''SELECT username, password FROM information
                   WHERE username=? AND password=?''', (USERNAME_VERIFICATION.get(),
                                                        PASSWORD_VERIFICATION.get()))
    row = CURSOR.fetchone()
    if row:
        WINDOW.destroy()
    else:
        error()

def error():
    """Hoitaa ongelman, jos väärä salasana tai käyttäjätunnus.
    """
    messagebox.showerror("Error", "Invalid username or password")

LOGIN_WINDOW = LogInView(WINDOW)
LOGIN_WINDOW.start()

WINDOW.mainloop()
CONNECT.close()
