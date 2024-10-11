import tkinter as tk
from tkinter import ttk
import csv

def First():
    window = tk.Tk()
    window.title("First Page")
    label = tk.Label(window, text="First Window")
    label.pack()


    


    def Reg_Form():
        window1 = tk.Tk()
        window.destroy()
        window1.title("Registration Form")
        window1.geometry("300x200")

        label1 = tk.Label(window1, text="Name")
        label1.pack()
        label1_entry=tk.Entry(window1)
        label1_entry.pack()

        label2 = tk.Label(window1, text="Age")
        label2.pack()
        label2_entry=tk.Entry(window1)
        label2_entry.pack()

        label3 = tk.Label(window1, text="Gender")
        label3.pack()
        label3_entry=tk.Entry(window1)
        label3_entry.pack()
        

        label4 = tk.Label(window1, text="Email")
        label4.pack()
        label4_entry=tk.Entry(window1)
        label4_entry.pack()

        def submit_registration():
            Name = label1_entry.get()
            Age = label2_entry.get()
            Gender = label3_entry.get()
            Email=label4_entry.get()
                
        # Create a CSV file and write the registration data to it
            with open('registrations.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([Name, Age, Gender,Email])


        def third():
            window2 = tk.Tk()
            window1.destroy()
            label5 = tk.Label(window2, text="Form Submitted Successfully")
            label5.pack()
            






        button = tk.Button(window1, text="Submit", command=third)
        button.pack()
    


    def Pre_Data():
        root = tk.Tk()
        window.destroy()
        root.title("CSV Data Viewer")

            # Create a Treeview widget to display the data
        tree = ttk.Treeview(root)

            # Define the columns
        tree['columns'] = ('Name', 'Age', 'Gender','Email')

            # Format the columns
        tree.column("#0", width=0, stretch=tk.NO)
        tree.column("Name", anchor=tk.W, width=100)
        tree.column("Age", anchor=tk.W, width=50)
        tree.column("Gender", anchor=tk.W, width=50)
        tree.column("Email", anchor=tk.W, width=50)

            # Create headings
        tree.heading("#0", text="", anchor=tk.W)
        tree.heading("Name", text="Name", anchor=tk.W)
        tree.heading("Age", text="Age", anchor=tk.W)
        tree.heading("Gender", text="Gender", anchor=tk.W)
        tree.heading("Email", text="EMail", anchor=tk.W)

            # Read data from the CSV file
        with open('registrations.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                tree.insert('', 'end', values=row)

            # Add the Treeview widget to the GUI window
        tree.pack()


        


    button1 = tk.Button(window, text="Add New Data",command=Reg_Form)
    button1.pack()
    button2 = tk.Button(window, text="Show Previous Data",command=Pre_Data)
    button2.pack()
  
    button4 = tk.Button(window2, text="OK", command=First)
    button4.pack()



    window.mainloop()




