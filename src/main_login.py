from calendar import c
from login import *
from tkinter import messagebox

connect = sqlite3.connect(os.path.join("login_information.db"))
cursor = connect.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS information(username TEXT, email TEXT, password TEXT)''')
connect.commit()


def login():
    cursor.execute("SELECT username, password FROM information WHERE username=? AND password=?", (username_verification.get(), password_verification.get()))
    row = cursor.fetchone()
    if row:
        window.destroy()
    else:
        error()
        
        
def register():
    global register_screen
    global username, password, email
    register_screen = Toplevel(window)
    register_screen.title("Register")
    register_screen.geometry("300x200")
    register_screen.configure(bg='#B0E0E6')
    username = StringVar()
    password = StringVar()
    email = StringVar()

    label = Label(register_screen, text="Enter information", bg='#B0E0E6', font=FONT)

    username_label = Label(register_screen, text="Username: ", bg='#B0E0E6')
    email_label = Label(register_screen, text="Email: ", bg='#B0E0E6')
    password_label = Label(register_screen, text="Password: ", bg='#B0E0E6')

    username_entry = Entry(register_screen, textvariable=username, bg='#7BD5D5')
    email_entry = Entry(register_screen, textvariable=email, bg='#7BD5D5')
    password_entry = Entry(register_screen, textvariable=password, bg='#7BD5D5')
    
    button = Button(register_screen, text="Register", width=10, height=1, bg='#56BACE', font=FONT, command=add_to_database)

    label.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
    username_label.grid(padx=5, pady=5)
    username_entry.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
    email_label.grid(padx=5, pady=5)
    email_entry.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
    password_label.grid(padx=5, pady=5)
    password_entry.grid(row=3, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

    button.grid(columnspan=2, sticky=(constants.E,constants.W), padx=5, pady=5)

    
def add_to_database():
    flag_validation=True
    cursor.execute("INSERT INTO information VALUES (:username, :email, :password)", {
            'username': username.get(), 
            'email': email.get(),
            'password': password.get()
            })
    connect.commit()
    connect.close()       
        
    
def error():
    messagebox.showerror("Error", "Invalid username or password")

class LogInView:
    def __init__(self, root):
        self._root = root
    def start(self):
        self._frame = tk.Frame(master=self._root)
        global username_verification
        global password_verification
        heading = tk.Label(master=self._root, text="Login or Register", bg="#B0E0E6", font=FONT)  
        username_verification = StringVar()
        password_verification = StringVar() 
        username = tk.Label(master=self._root, text="Username", bg='#B0E0E6')
        username_entry = tk.Entry(master=self._root, bg ='#7BD5D5', textvariable=username_verification)
        password = tk.Label(master=self._root, text="Password", bg='#B0E0E6')
        password_entry = tk.Entry(master=self._root, bg='#7BD5D5', textvariable=password_verification)

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

