# rounds.py
"""
Handles round logic for best of 3 gameplay in Rock-Paper-Scissors-Lizard-Spock.
"""

class RoundsManager:
    def __init__(self, total_rounds=3):
        self.total_rounds = total_rounds
        self.current_round = 1
        self.scores = [0, 0]  # [Player1, Player2/Computer]

    def next_round(self):
        self.current_round += 1

    def add_score(self, winner):
        if winner in [0, 1]:
            self.scores[winner] += 1

    def is_game_over(self):
        return self.current_round > self.total_rounds

    def get_winner(self):
        if self.scores[0] > self.scores[1]:
            return 0
        elif self.scores[1] > self.scores[0]:
            return 1
        else:
            return -1  # Tie
