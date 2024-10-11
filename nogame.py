import tkinter as tk
from random import randint


# def open_second_window():
#     window1.destroy()  # Close the first window



window1 = tk.Tk()
window1.title("Window 1")
window1.geometry("300x200")
label1 = tk.Label(window1, text="Enter the amount")
label1.pack()
label1_entry=tk.Entry(window1)
label1_entry.pack()







def Guess_Game():
    window1.destroy()       # Close the first window
    root = tk.Tk()
    root.title("Number Guessing Game")
        

def generate_num(self):
    self.otp = str(randint(0, 9))
    self.otp_label['text'] = f"Random Number: {self.otp}"
            

def check_result(self):
    user_otp = self.verify_entry.get()
    if user_otp==self.otp:
        self.result_label['text'] = "You Won \n Number Matched successfully!"
    else:
        self.result_label['text'] = "You Lose \n Number not Matched!"


     # Create GUI elements
    label = tk.Label(root, text="Number Guessing Game")
    label.pack()
        
    verify_label = tk.Label(root, text="Enter Number(0-9): ")
    verify_label.pack()

    verify_entry = tk.Entry(root,show='*')
    verify_entry.pack()

       

    generate_button = tk.Button(root, text="Generate Number", command=generate_num)
    generate_button.pack()

    otp_label = tk.Label(root, text="Number: ")
    otp_label.pack()


    verify_button = tk.Button(root, text="Check Result", command=check_result)
    verify_button.pack()

    result_label = tk.Label(root, text="")
    result_label.pack()

        
button1 = tk.Button(window1, text="Open game",command=Guess_Game)
button1.pack()

window1.mainloop()
