import tkinter as tk
import random

# Generate the secret number
secret_number = random.randint(1, 100)

def check_guess():
    try:
        guess = int(entry.get())
        if guess < secret_number:
            result_label.config(text="Too low!")
        elif guess > secret_number:
            result_label.config(text="Too high!")
        else:
            result_label.config(text="You guessed it! 🎉")
    except ValueError:
        result_label.config(text="Please enter a valid number.")

# Create the main window
root = tk.Tk()
root.title("Number Guessing Game")

# GUI layout
tk.Label(root, text="Guess a number between 1 and 100:").pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Guess", command=check_guess).pack(pady=5)
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Start the GUI event loop
root.mainloop()