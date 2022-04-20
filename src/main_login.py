from login import *
import mysql.connector


database = mysql.connector.connect(
    host = "localhost",
    user = "user",
    password = "password",
    database = "login_information"
)
cursor = database.cursor()



window.geometry("400x200")
window.title("Login")
window.configure(bg='#B0E0E6')



class LogInView:
    def __init__(self, root):
        self._root = root
    def start(self):
        self._frame = tk.Frame(master=self._root)
        heading = tk.Label(master=self._root, text="Login or Register", bg="#B0E0E6", font=FONT)   
        username = tk.Label(master=self._root, text="Username", bg='#B0E0E6')
        username_entry = tk.Entry(master=self._root, bg ='#7BD5D5')
        password = tk.Label(master=self._root, text="Password", bg='#B0E0E6')
        password_entry = tk.Entry(master=self._root, bg='#7BD5D5')

        button = tk.Button(master=self._root, text="Start game", bg='#56BACE',
                           command=verification, font=FONT)
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

