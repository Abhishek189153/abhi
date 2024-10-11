import tkinter as tk
from random import randint

def Guess_Game():
    # window.destroy()  # Close the first window
    root = tk.Tk()
    root.title("Number Guessing Game")

    otp = None  # Define otp variable
    otp_label = tk.Label(root, text="Number: ")
    otp_label.pack()

    verify_entry = tk.Entry(root, show='*')
    verify_entry.pack()

    result_label = tk.Label(root, text="")
    result_label.pack()

    def generate_num():
        nonlocal otp  # Use nonlocal keyword to access otp variable
        otp = str(randint(0, 9))
        otp_label['text'] = f"Random Number: {otp}"

    def check_result():
        nonlocal otp  # Use nonlocal keyword to access otp variable
        user_otp = verify_entry.get()
        if user_otp == otp:
            result_label['text'] = "You Won \n Number Matched successfully!"
        else:
            result_label['text'] = "You Lose \n Number not Matched!"

    generate_button = tk.Button(root, text="Generate Number", command=generate_num)
    generate_button.pack()

    verify_button = tk.Button(root, text="Check Result", command=check_result)
    verify_button.pack()

    root.mainloop()

    Guess_Game()