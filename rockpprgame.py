import tkinter as tk
from random import choice
# from random import randint
# import time

class RPS_Game:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Rock,paper,Scissor Game")
        

        # Create GUI elements
        self.label = tk.Label(self.root, text="Rock,Paper,Scissor Game")
        self.label.pack()

        self.generate_button = tk.Button(self.root, text="Rock", command=self.rock)
        self.generate_button.pack()

        self.generate_button = tk.Button(self.root, text="Paper", command=self.paper)
        self.generate_button.pack()

        self.generate_button = tk.Button(self.root, text="Scissor", command=self.scissor)
        self.generate_button.pack()

        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset)
        self.reset_button.pack()

        

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

       
    def computer_choice(self):
        return choice(["Rock", "Paper", "Scissors"])
    
    def rock(self):
        computer = self.computer_choice()
        if computer == "Rock":
            self.result_label['text'] = "It's a tie!"
        elif computer == "Paper":
           self.result_label['text'] = "Paper covers Rock! Computer won!"
        else:
            self.result_label['text'] = "Rock smashes Scissors! You won!"


    def paper(self):
        computer = self.computer_choice()
        if computer == "Paper":
            self.result_label['text'] = "It's a tie!"
        elif computer == "Scissors":
           self.result_label['text'] = "Scissors cuts Paper! Computer won!"
        else:
           self.result_label['text'] = "Paper covers Rock! You won!"


    def scissor(self):
        computer = self.computer_choice()
        if computer == "Scissors":
            self.result_label['text'] = "It's a tie!"
        elif computer == "Rock":
            self.result_label['text'] = "Rock smashes Scissors! Computer won!"
        else:
            self.result_label['text'] = "Scissors cuts Paper! You won!"

    def reset(self):
            self.result_label['text'] = ""

         
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = RPS_Game()
    game.run()


