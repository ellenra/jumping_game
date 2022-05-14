from tkinter import Label, Entry, Button, StringVar, constants, Toplevel, messagebox
from login.login_settings import WINDOW, FONT, CURSOR, CONNECT

USERNAME = 1
PASSWORD = 1
EMAIL = 1

def register():
    """Luo rekisteri-ikkunan ja hallinnassa sen toiminnasta.
    """
    global USERNAME, PASSWORD, EMAIL

    register_screen = Toplevel(WINDOW)
    register_screen.title("Register")
    register_screen.geometry("300x200")
    register_screen.configure(bg='#B0E0E6')

    USERNAME = StringVar()
    PASSWORD = StringVar()
    EMAIL = StringVar()

    label = Label(register_screen, text="Enter information", bg='#B0E0E6', font=FONT)

    username_label = Label(register_screen, text="Username: ", bg='#B0E0E6')
    email_label = Label(register_screen, text="Email: ", bg='#B0E0E6')
    password_label = Label(register_screen, text="Password: ", bg='#B0E0E6')

    username_entry = Entry(register_screen, textvariable=USERNAME, bg='#7BD5D5')
    email_entry = Entry(register_screen, textvariable=EMAIL, bg='#7BD5D5')
    password_entry = Entry(register_screen, textvariable=PASSWORD, bg='#7BD5D5')

    button = Button(register_screen, text="Register", width=10, height=1, bg='#56BACE',
                    font=FONT, command=test_errors)

    label.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
    username_label.grid(padx=5, pady=5)
    username_entry.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

    email_label.grid(padx=5, pady=5)
    email_entry.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

    password_label.grid(padx=5, pady=5)
    password_entry.grid(row=3, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

    button.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

def test_errors():
    """Funktio, joka varmistaa, että tiedot ovat sopivia
    """
    usnam = USERNAME.get()
    email = EMAIL.get()
    paswrd = PASSWORD.get()
    while True:
        if len(usnam) < 2:
            register_error()
            return
        if len(email) < 4:
            register_error()
            return
        if len(paswrd) < 2:
            register_error()
            return
        add_to_database()


def add_to_database():
    """Lisää käyttäjän tiedot tietokantaan.
    """
    CURSOR.execute("INSERT INTO information VALUES (:username, :email, :password)", {
        'username': USERNAME.get(),
        'email': EMAIL.get(),
        'password': PASSWORD.get()
        })
    CONNECT.commit()
    WINDOW.destroy()

def register_error():
    """Hoitaa ongelman, jos vääränlainen salasana, mail tai käyttäjätunnus.
    """
    messagebox.showerror("Error", "Invalid information, try again.")
