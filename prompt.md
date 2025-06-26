# Rock-Paper-Scissors-Lizard-Spock Game Development Log

## Date: 2025-06-26

### Initial Questions for User

1. **Game Mode**: Should the game be single-player (user vs computer), two-player (user vs user), or support both?
   - **User Answer (2025-06-26):** The game mode must be both.
2. **User Interface**: Do you want a command-line interface, a graphical user interface, or a web-based interface?
   - **User Answer (2025-06-26):** A graphical user interface.
3. **Number of Rounds**: Should the game be best-of-N rounds, or just a single round per play?
   - **User Answer (2025-06-26):** Number of rounds should be 3 (best of 3).
4. **Score Tracking**: Should the game keep track of scores across rounds or just display the winner of each round?
   - **User Answer (2025-06-26):** Keep track of scores across rounds.
5. **Replay Option**: Should the user be able to play again after a game ends?
   - **User Answer (2025-06-26):** The user should be able to replay.
6. **Rules Display**: Should the game display the rules or a help menu?
   - **User Answer (2025-06-26):** The game must display the rules.
7. **Input Validation**: Should the game handle invalid inputs gracefully and prompt the user again?
   - **User Answer (2025-06-26):** The game must handle invalid inputs gracefully.
8. **Additional Features**: Are there any extra features you want (e.g., sound effects, saving high scores, etc.)?
   - **User Answer (2025-06-26):** There must be sound effects, high scores must be saved, users must enter names before the game begins and the names must be used in the high score list. I would also like a Halloween theme.

---

## 2025-06-26: Progress Log
- [x] Environment prepared and Draw.io extension installed (see checklist.md)
- [x] Support both single-player (user vs computer) and two-player (user vs user) modes (see game_modes.py)
- [x] Graphical user interface (GUI) started with Tkinter (see gui.py)
- [x] Best of 3 rounds per game logic created (see rounds.py)
- [x] Score tracking across rounds managed by RoundsManager (see rounds.py)
- [x] Replay option after a game ends added to GUI (see gui.py)
- [x] Rules defined in rules.py, referencing the image in assets
- [x] Rules display added to GUI (see gui.py)
- [x] Input validation added to GUI (see gui.py)
- [x] Sound effects module created and playsound installed (see sound.py)
- [x] High scores module created (see high_scores.py)
- [x] Name entry required before game begins (see gui.py)
- [x] Player names used in high score list (see high_scores.py)
- [x] Halloween theme applied to GUI (see gui.py)

All user answers above are now recorded. All further prompts and actions will be recorded in this file for your reference.
