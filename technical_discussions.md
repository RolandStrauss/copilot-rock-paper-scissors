# Technical Discussions: Rock-Paper-Scissors-Lizard-Spock Game

## Technology Stack
- Python 3.x
- GUI: Tkinter (standard), or PyQt5 if advanced visuals are needed
- Sound: pygame or playsound
- Data persistence: JSON or SQLite for high scores
- Unit testing: pytest
- Diagrams: draw.io (system_flow.io)

## Key Design Decisions
- Use a GUI for user interaction to meet requirements and enhance user experience.
- Store high scores in a persistent file (JSON or SQLite) for easy access and update.
- Use a modular approach: separate game logic, GUI, sound, and data persistence.
- Halloween theme: custom colors, fonts, and images for GUI.
- Sound effects: triggered on win/loss/tie and button clicks.
- Usernames required before game start; used in high score list.
- Rules referenced from provided image asset.

## Open Questions / Risks
- Which GUI toolkit: Tkinter (simple, built-in) vs PyQt5 (more advanced, requires install)?
- Sound library compatibility across platforms.
- Handling concurrent access to high score file (if multiplayer on same machine).
- REST API (optional): Flask or FastAPI if implemented.

## Next Steps
- Confirm GUI toolkit and sound library.
- Design system flow diagram in draw.io.
- Begin modular implementation.

---
This document will be updated as technical decisions are made.
