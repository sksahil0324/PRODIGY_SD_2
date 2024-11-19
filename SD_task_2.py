import tkinter as tk
from tkinter import ttk, messagebox
import random

random_number = random.randint(1, 100)
attempts = 0

def check_guess():
    global attempts, random_number
    try:
        guess = int(entry_guess.get())
        attempts += 1

        difference = abs(random_number - guess)

        if guess < random_number:
            if difference > 20:
                feedback_label.config(text="Too low! You're far off.", foreground="blue")
            else:
                feedback_label.config(text="Too low! You're close.", foreground="blue")
        elif guess > random_number:
            if difference > 20:
                feedback_label.config(text="Too high! You're far off.", foreground="red")
            else:
                feedback_label.config(text="Too high! You're close.", foreground="red")
        else:
            messagebox.showinfo("Congratulations!", f"You guessed it! The number was {random_number}.\nIt took you {attempts} attempts.")
            reset_game()
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

def reset_game():
    global random_number, attempts
    random_number = random.randint(1, 100)
    attempts = 0
    feedback_label.config(text="Guess a number between 1 and 100.", foreground="black")
    entry_guess.delete(0, tk.END)

root = tk.Tk()
root.title("Number Guessing Game")

instruction_label = ttk.Label(root, text="I have picked a number between 1 and 100. Can you guess it?", font=("Arial", 12))
instruction_label.pack(pady=10)

frame_input = ttk.Frame(root, padding=10)
frame_input.pack(pady=10)

ttk.Label(frame_input, text="Enter your guess:").grid(row=0, column=0, padx=5, sticky="w")
entry_guess = ttk.Entry(frame_input, width=20)
entry_guess.grid(row=0, column=1, padx=5)

frame_buttons = ttk.Frame(root, padding=10)
frame_buttons.pack()

check_button = ttk.Button(frame_buttons, text="Check", command=check_guess)
check_button.grid(row=0, column=0, padx=5)

reset_button = ttk.Button(frame_buttons, text="Reset", command=reset_game)
reset_button.grid(row=0, column=1, padx=5)

exit_button = ttk.Button(frame_buttons, text="Exit", command=root.quit)
exit_button.grid(row=0, column=2, padx=5)

feedback_label = ttk.Label(root, text="Guess a number between 1 and 100.", font=("Arial", 12), foreground="black")
feedback_label.pack(pady=10)

root.mainloop()
