import tkinter as tk
from tkinter import messagebox
from random import randint

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




def open_second_window():
    window.destroy()  # Close the first window
    window1 = tk.Tk()
    window1.title("Window 1")
    window1.geometry("300x200")
    label1 = tk.Label(window1, text="Enter the amount")
    label1.pack()
    label1_entry=tk.Entry(window1)
    label1_entry.pack()

    
    def open_third_window():
        window1.destroy()  # Close the second window
        root = tk.Tk()
        root.title("Number Guessing Game")

        # Set the secret number
        secret_number = randint(0, 9)

        # Create a label to display the instructions
        instructions_label = tk.Label(root, text="Guess a number between 0 and 9:")
        instructions_label.pack()

        # Create an entry field for the user to input their guess
        guess_entry = tk.Entry(root)
        guess_entry.pack()

        # Create a label to display the result
        result_label = tk.Label(root, text="")
        result_label.pack()

        # Define a function to check the user's guess
        def check_guess():
            user_guess = int(guess_entry.get())
            if user_guess == secret_number:
                result_label.config(text=" Congratulations! You guessed the number!")
            else:
                result_label.config(text="wrong! Try again")

        def reset():
            result_label['text'] = ""

            
        # Create a button to submit the user's guess
        submit_button = tk.Button(root, text="Submit", command=check_guess)
        submit_button.pack()
        reset_button = tk.Button(root, text="Reset", command=reset)
        reset_button.pack()

        
    button1=tk.Button(window1,text="submit",command=open_third_window)
    button1.pack()






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



button=tk.Button(window,text="submit",command=open_second_window)
button.pack()
window.mainloop()
