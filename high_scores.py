# high_scores.py
"""
Handles saving and loading high scores for the game using a JSON file.
"""
import json
import os

HIGH_SCORES_FILE = "high_scores.json"


def load_high_scores():
    if not os.path.exists(HIGH_SCORES_FILE):
        return []
    with open(HIGH_SCORES_FILE, "r") as f:
        return json.load(f)


def save_high_score(name, score):
    scores = load_high_scores()
    scores.append({"name": name, "score": score})
    scores = sorted(scores, key=lambda x: x["score"], reverse=True)[:10]  # Keep top 10
    with open(HIGH_SCORES_FILE, "w") as f:
        json.dump(scores, f, indent=2)


def get_high_scores():
    return load_high_scores()
