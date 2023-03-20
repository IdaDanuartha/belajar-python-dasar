# GUI -> Graphical User Interface

# import library tkinter
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# initialize object Tk()
app = tk.Tk()

# configuration app
app.configure(bg="white")
app.geometry("600x400")
app.resizable(False, False)
app.title("Simple GUI App")

# frame input
input_frame = ttk.Frame(app)

# penempatan Grid, Pack, Place
input_frame.pack(padx=10, pady=10, fill="x", expand=True)

# komponen - komponen
# 1. Label username
username_label = ttk.Label(input_frame, text="Username")
username_label.pack(padx=10, fill="x", expand=True)

# entry username
USERNAME = tk.StringVar()
username_entry = ttk.Entry(input_frame, textvariable=USERNAME)
username_entry.pack(padx=10, fill="x", expand=True)

# 2. Label password
password_label = ttk.Label(input_frame, text="Password")
password_label.pack(padx=10, fill="x", expand=True)

# entry nama belakang
PASSWORD = tk.StringVar()
password_entry = ttk.Entry(input_frame, textvariable=PASSWORD)
password_entry.pack(padx=10, fill="x", expand=True)

# 3. Button
def login():
    print(USERNAME.get())
    msg = f'''
    Username = {USERNAME.get()}
    Password = {PASSWORD.get()}
    '''

    showinfo(title="Login Successfully!", message=msg)

submit_btn = ttk.Button(input_frame, text="Login", command=login)
submit_btn.pack(fill="x", expand=True, padx=10, pady=10)

app.mainloop()