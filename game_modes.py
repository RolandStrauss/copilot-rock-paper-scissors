# game_modes.py

"""
Module to support both single-player (user vs computer) and two-player (user vs user) modes for the Rock-Paper-Scissors-Lizard-Spock game.
"""

import random

OPTIONS = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

def get_computer_choice():
    return random.choice(OPTIONS)

# Placeholder for player name input and game mode selection logic
# This module will be integrated with the GUI in the next steps.
