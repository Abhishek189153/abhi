import tkinter as tk
from random import choice

class RockPaperScissors:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Rock Paper Scissors")
        self.root.geometry("300x300")

        self.player_score = 0
        self.computer_score = 0

        self.player_score_label = tk.Label(self.root, text="Player Score: 0", font=("Arial", 12))
        self.player_score_label.pack()

        self.computer_score_label = tk.Label(self.root, text="Computer Score: 0", font=("Arial", 12))
        self.computer_score_label.pack()

        self.result_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.result_label.pack()

        self.rock_button = tk.Button(self.root, text="Rock", command=self.rock)
        self.rock_button.pack()

        self.paper_button = tk.Button(self.root, text="Paper", command=self.paper)
        self.paper_button.pack()

        self.scissors_button = tk.Button(self.root, text="Scissors", command=self.scissors)
        self.scissors_button.pack()

        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset)
        self.reset_button.pack()

    def computer_choice(self):
        return choice(["Rock", "Paper", "Scissors"])

    def rock(self):
        computer = self.computer_choice()
        if computer == "Rock":
            self.result_label['text'] = "It's a tie!"
        elif computer == "Paper":
            self.computer_score += 1
            self.computer_score_label['text'] = f"Computer Score: {self.computer_score}"
            self.result_label['text'] = "Paper covers Rock! Computer wins!"
        else:
            self.player_score += 1
            self.player_score_label['text'] = f"Player Score: {self.player_score}"
            self.result_label['text'] = "Rock smashes Scissors! Player wins!"

    def paper(self):
        computer = self.computer_choice()
        if computer == "Paper":
            self.result_label['text'] = "It's a tie!"
        elif computer == "Scissors":
            self.computer_score += 1
            self.computer_score_label['text'] = f"Computer Score: {self.computer_score}"
            self.result_label['text'] = "Scissors cuts Paper! Computer wins!"
        else:
            self.player_score += 1
            self.player_score_label['text'] = f"Player Score: {self.player_score}"
            self.result_label['text'] = "Paper covers Rock! Player wins!"

    def scissors(self):
        computer = self.computer_choice()
        if computer == "Scissors":
            self.result_label['text'] = "It's a tie!"
        elif computer == "Rock":
            self.computer_score += 1
            self.computer_score_label['text'] = f"Computer Score: {self.computer_score}"
            self.result_label['text'] = "Rock smashes Scissors! Computer wins!"
        else:
            self.player_score += 1
            self.player_score_label['text'] = f"Player Score: {self.player_score}"
            self.result_label['text'] = "Scissors cuts Paper! Player wins!"

    def reset(self):
        self.player_score = 0
        self.computer_score = 0
        self.player_score_label['text'] = "Player Score: 0"
        self.computer_score_label['text'] = "Computer Score: 0"
        self.result_label['text'] = ""

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = RockPaperScissors()
    game.run()