import tkinter as tk
from tkinter import messagebox
def verify_pass():
    username="Abhishek"
    password="12345"
    user_input=entry.get()
    user_input

    
    if user_input==password and user_input!=username:
        messagebox.showinfo(" Password is verified but incorrect username")
    elif user_input==username and user_input!=password:
        messagebox.showinfo(" Username is verified but incorrect Password")
    elif user_input!=username and user_input!=password:
        messagebox.showinfo(" Both Username and Password is incorrect")
    elif user_input==username and user_input==password:
        messagebox.showinfo(" Both Username and Password is verified")


window=tk.Tk()
window.title("Login Form")
label=tk.Label(window,text="Enter Username")
label.pack()
entry=tk.Entry(window)
entry.pack()
label=tk.Label(window,text="Enter Password")
label.pack()
entry=tk.Entry(window,show='*')
entry.pack()
button=tk.Button(window,text="submit", command=verify_pass)
button.pack()
window.mainloop()
