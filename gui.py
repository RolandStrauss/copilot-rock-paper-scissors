# gui.py
"""
Tkinter-based GUI for Rock-Paper-Scissors-Lizard-Spock game.
Supports single-player and two-player modes, user name entry, and is themed for Halloween.
"""
import tkinter as tk
from tkinter import messagebox
from rules import RULES_TEXT, RULES

class RPSLSApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Rock-Paper-Scissors-Lizard-Spock (Halloween Edition)")
        self.geometry("600x500")
        self.configure(bg="#2d1b2d")  # Halloween dark purple
        self.player1_name = tk.StringVar()
        self.player2_name = tk.StringVar()
        self.name_frame = tk.Frame(self, bg="#2d1b2d")
        tk.Label(self.name_frame, text="Enter Player 1 Name:", fg="#fff", bg="#2d1b2d", font=("Creepster", 14, "bold")).pack(pady=5)
        tk.Entry(self.name_frame, textvariable=self.player1_name, font=("Arial", 12)).pack(pady=5)
        tk.Label(self.name_frame, text="Enter Player 2 Name (or leave blank for computer):", fg="#fff", bg="#2d1b2d", font=("Creepster", 14, "bold")).pack(pady=5)
        tk.Entry(self.name_frame, textvariable=self.player2_name, font=("Arial", 12)).pack(pady=5)
        tk.Button(self.name_frame, text="Start Game", command=self.start_game, fg="#fff", bg="#ff7518", font=("Arial", 12, "bold"), activebackground="#ff7518", activeforeground="#2d1b2d").pack(pady=10)
        self.name_frame.pack(pady=20)
        # Rules button
        self.rules_button = tk.Button(self, text="Show Rules", command=self.show_rules, fg="#fff", bg="#ff7518", font=("Arial", 14, "bold"), activebackground="#ff7518", activeforeground="#2d1b2d")
        # Replay button
        self.replay_button = tk.Button(self, text="Replay", command=self.replay_game, fg="#fff", bg="#ff7518", font=("Arial", 14, "bold"), activebackground="#ff7518", activeforeground="#2d1b2d")
        self.replay_button.pack_forget()  # Hide initially
        # Input for player move (for demonstration)
        self.input_label = tk.Label(self, text="Enter your move (Rock, Paper, Scissors, Lizard, Spock):", fg="#fff", bg="#2d1b2d", font=("Arial", 12))
        self.input_label.pack(pady=5)
        self.input_entry = tk.Entry(self, font=("Arial", 12))
        self.input_entry.pack(pady=5)
        self.submit_button = tk.Button(self, text="Submit Move", command=self.handle_move, fg="#fff", bg="#ff7518", font=("Arial", 12, "bold"))
        self.submit_button.pack(pady=5)
        # Add a Halloween-themed label at the bottom
        self.halloween_label = tk.Label(self, text="🎃 Happy Halloween! 🎃", fg="#ff7518", bg="#2d1b2d", font=("Creepster", 20, "bold"))
        self.halloween_label.pack(side="bottom", pady=10)

    def show_rules(self):
        messagebox.showinfo("Game Rules", RULES_TEXT)

    def show_replay(self):
        self.replay_button.pack(pady=10)

    def hide_replay(self):
        self.replay_button.pack_forget()

    def replay_game(self):
        self.hide_replay()
        messagebox.showinfo("Replay", "Game has been reset! (Implement full reset logic)")

    def handle_move(self):
        move = self.input_entry.get().capitalize()
        if move not in RULES:
            messagebox.showerror("Invalid Input", f"'{move}' is not a valid move. Please enter Rock, Paper, Scissors, Lizard, or Spock.")
        else:
            messagebox.showinfo("Valid Move", f"You entered: {move}")

    def start_game(self):
        if not self.player1_name.get().strip():
            messagebox.showerror("Input Error", "Player 1 name is required.")
            return
        # Hide name entry and show main game UI
        self.name_frame.pack_forget()
        self.rules_button.pack(pady=10)
        self.replay_button.pack(pady=10)
        self.replay_button.pack_forget()
        # Additional logic to initialize game state can be added here

if __name__ == "__main__":
    app = RPSLSApp()
    app.mainloop()
