# import tkinter as tk

# def open_second_window():
#     window1.destroy()  # Close the first window
#     window2 = tk.Tk()
#     window2.title("Window 2")
#     window2.geometry("300x200")
#     label2 = tk.Label(window2, text="This is Window 2")
#     label2.pack()
#     window2.mainloop()

# # Create the first window
# window1 = tk.Tk()
# window1.title("Window 1")
# window1.geometry("300x200")
# label1 = tk.Label(window1, text="This is Window 1")
# label1.pack()

# # Create a button in the first window to open the second window
# button1 = tk.Button(window1, text="Open Window 2", command=open_second_window)
# button1.pack()

# window1.mainloop()











import tkinter as tk
from random import choice
# from random import randint
# import time


def RPS_Game():
    root = tk.Tk()
    root.title("Rock,paper,Scissor Game")
        

        # Create GUI elements
    label = tk.Label(root, text="Rock,Paper,Scissor Game")
    label.pack()

    generate_button = tk.Button(root, text="Rock", command=rock)
    generate_button.pack()

    generate_button = tk.Button(root, text="Paper", command=paper)
    generate_button.pack()

    generate_button = tk.Button(root, text="Scissor", command=scissor)
    generate_button.pack()

    reset_button = tk.Button(root, text="Reset", command=reset)
    reset_button.pack()

        

    result_label = tk.Label(root, text="")
    result_label.pack()

       
def computer_choice():
        return choice(["Rock", "Paper", "Scissors"])
    
def rock():
    computer = computer_choice()
    if computer == "Rock":
        result_label['text'] = "It's a tie!"
    elif computer == "Paper":
        result_label['text'] = "Paper covers Rock! Computer won!"
    else:
        result_label['text'] = "Rock smashes Scissors! You won!"


def paper():
    computer = computer_choice()
    if computer == "Paper":
        result_label['text'] = "It's a tie!"
    elif computer == "Scissors":
        result_label['text'] = "Scissors cuts Paper! Computer won!"
    else:
        result_label['text'] = "Paper covers Rock! You won!"


def scissor(self):
    computer = self.computer_choice()
    if computer == "Scissors":
        result_label['text'] = "It's a tie!"
    elif computer == "Rock":
        result_label['text'] = "Rock smashes Scissors! Computer won!"
    else:
        result_label['text'] = "Scissors cuts Paper! You won!"

def reset():
    result_label['text'] = ""

         
def run():
    root.mainloop()

# if __name__ == "__main__":
#     game = RPS_Game()
#     game.run()


