# sound.py
"""
Handles sound effects for game actions using the playsound library.
"""
from playsound import playsound
import os

SOUNDS = {
    "win": "assets/win.wav",
    "lose": "assets/lose.wav",
    "tie": "assets/tie.wav",
    "click": "assets/click.wav"
}

def play_sound(event):
    sound_file = SOUNDS.get(event)
    if sound_file and os.path.exists(sound_file):
        playsound(sound_file, block=False)
