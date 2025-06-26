# rules.py
"""
Defines the rules for Rock-Paper-Scissors-Lizard-Spock, referencing the image in the assets folder.
"""

RULES = {
    "Rock":     ["Scissors", "Lizard"],
    "Paper":    ["Rock", "Spock"],
    "Scissors": ["Paper", "Lizard"],
    "Lizard":   ["Spock", "Paper"],
    "Spock":    ["Scissors", "Rock"]
}

RULES_TEXT = """
Rock crushes Scissors
Scissors cuts Paper
Paper covers Rock
Rock crushes Lizard
Lizard poisons Spock
Spock smashes Scissors
Scissors decapitates Lizard
Lizard eats Paper
Paper disproves Spock
Spock vaporizes Rock
"""

# Reference: See 'assets/Rock Paper Scissors Lizard Spock image.jpg' for a visual representation.
