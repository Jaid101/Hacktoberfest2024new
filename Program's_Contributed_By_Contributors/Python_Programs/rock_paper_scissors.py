import tkinter as tk
from random import choice

# Main game logic
def play(user_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = choice(choices)
    
    if user_choice == computer_choice:
        result = "It's a Draw!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        result = "You Win!"
    else:
        result = "You Lose!"
    
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

# Setting up the GUI
root = tk.Tk()
root.title("Rock Paper Scissors")

# Title
title_label = tk.Label(root, text="Rock Paper Scissors", font=('Helvetica', 18, 'bold'))
title_label.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=('Helvetica', 14))
result_label.pack(pady=20)

# Buttons for Rock, Paper, Scissors
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

rock_button = tk.Button(button_frame, text="Rock", font=('Helvetica', 12), width=10, command=lambda: play('Rock'))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper", font=('Helvetica', 12), width=10, command=lambda: play('Paper'))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors", font=('Helvetica', 12), width=10, command=lambda: play('Scissors'))
scissors_button.grid(row=0, column=2, padx=10)

# Run the GUI
root.mainloop()
