# from tkinter import *
# root = Tk()
# w = Label(root, text='Computer Guru Training Institute')
# w.pack()
# root.title('Pushpendra bisht')


# root.mainloop()





# import tkinter as tk

# r = tk.Tk()
# r.title('Computer Guru')
# w = tk.Label( text='Computer Guru Training Institute')
# w.pack()

# button = tk.Button(r, text='Stop', width=25, command=r.destroy)
# button.pack()
# r.mainloop()


# from tkinter import *

# master = Tk()

# # master.title('Registration Form')
# w = Label(text='Computer Guru Training Institute')


# Label(master, text='First Name').grid(row=0)
# Label(master, text='Middle Name').grid(row=1)
# Label(master, text='Last Name').grid(row=2)
# e1 = Entry(master)
# e2 = Entry(master)
# e3 = Entry(master)
# e1.grid(row=0, column=1)
# e2.grid(row=1, column=1)
# e3.grid(row=2, column=1)
# w.pack()
# mainloop()





# if user_input==password and user_input!=username:
#         messagebox.showinfo(" Password is verified but incorrect username")
#     elif user_input==username and user_input!=password:
#         messagebox.showinfo(" Username is verified but incorrect Password")
#     elif user_input!=username and user_input!=password:
#         messagebox.showinfo(" Both Username and Password is incorrect")
#     elif user_input==username and user_input==password:
#         messagebox.showinfo(" Both Username and Password is verified")



# import tkinter as tk
# from tkinter import ttk
# import csv

# root = tk.Tk()
# root.title("Registration Form")

# label_name = ttk.Label(root, text="Name:")
# label_name.pack()

# name_entry = ttk.Entry(root, width=30)
# name_entry.pack()

# label_age = ttk.Label(root, text="Age:")
# label_age.pack()

# age_entry = ttk.Entry(root, width=30)
# age_entry.pack()

# label_gender = ttk.Label(root, text="Gender:")
# label_gender.pack()

# gender_var = tk.StringVar()
# gender_combobox = ttk.Combobox(root, textvariable=gender_var)
# gender_combobox['values'] = ('Male', 'Female', 'Other')
# gender_combobox.pack()

# def submit_registration():
#     name = name_entry.get()
#     age = age_entry.get()
#     gender = gender_var.get()
    
#     # Create a CSV file and write the registration data to it
#     with open('registrations.csv', 'a', newline='') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerow([name, age, gender])

# submit_button = ttk.Button(root, text="Submit", command=submit_registration)
# submit_button.pack()

# root.mainloop()


# import tkinter as tk
# from random import randint

# # Create the main window
# root = tk.Tk()
# root.title("Number Guessing Game")

# # Set the secret number
# secret_number = randint(0, 9)

# # Create a label to display the instructions
# instructions_label = tk.Label(root, text="Guess a number between 0 and 9:")
# instructions_label.pack()

# # Create an entry field for the user to input their guess
# guess_entry = tk.Entry(root)
# guess_entry.pack()



# # Create a label to display the result
# result_label = tk.Label(root, text="")
# result_label.pack()

# # Define a function to check the user's guess
# def check_guess():
#     user_guess = int(guess_entry.get())
#     if user_guess == secret_number:
#         result_label.config(text=" Congratulations! You guessed the number!")
#     else:
#         # result_label.config(text=secret_number)
#         result_label.config(text="wrong! Try again")

# def reset():
#     result_label['text'] = ""


#     # elif user_guess < secret_number:
#     #     result_label.config(text="Too low! Try again.")
#     # else:
#     #     result_label.config(text="Too high! Try again.")



# # Create a button to submit the user's guess
# submit_button = tk.Button(root, text="Submit", command=check_guess)
# submit_button.pack()
# reset_button = tk.Button(root, text="Reset", command=reset)
# reset_button.pack()

# # secret_label=tk.Label(root,text=secret_number)
# # secret_label.pack()

# # Start the GUI event loop
# root.mainloop()





import csv
import tkinter as tk
from tkinter import ttk

# Create a GUI window
root = tk.Tk()
root.title("CSV Data Viewer")

# Create a Treeview widget to display the data
tree = ttk.Treeview(root)

# Define the columns
tree['columns'] = ('Name', 'Age', 'Gender')

# Format the columns
# tree.column("#0", width=0, stretch=tk.NO)
# tree.column("Name", anchor=tk.W, width=100)
# tree.column("Age", anchor=tk.W, width=50)
# tree.column("Gender", anchor=tk.W, width=50)

# Create headings
tree.heading("#0", text="", anchor=tk.W)
tree.heading("Name", text="Name", anchor=tk.W)
tree.heading("Age", text="Age", anchor=tk.W)
tree.heading("Gender", text="Gender", anchor=tk.W)

# Read data from the CSV file
with open('registrations.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        tree.insert('', 'end', values=row)

# Add the Treeview widget to the GUI window
tree.pack()

# Run the GUI
root.mainloop()