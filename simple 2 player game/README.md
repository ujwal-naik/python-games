# 🚀 Space Clash: 2-Player Arcade Shooter

[![Python Version](https://shields.io)](https://python.org)
[![Framework](https://shields.io)](https://pygame.org)
[![License](https://shields.io)](#)

A fast-paced, **local multiplayer arcade game** built in Python using the Pygame library. Two players command specialized starships on opposite sides of the arena, maneuvering at high speeds to dodge incoming plasma fire while fighting to deplete the opponent's hull integrity.

---

## 🌟 Key Features

* **Instant Local Multiplayer:** Intense 1v1 action right on a single keyboard.
* **Tactical Arena Boundary:** A central energy barrier limits spaceships to their respective sectors, forcing strategic positioning.
* **Real-time Status Display:** Dynamic on-screen HUD tracking shield health for both players.
* **Immersive Spatial Audio:** Custom audio feedback for weapon firing and explosive hull impacts.
* **Infinite Arcade Loop:** The game automatically declares the victor and prepares the arena for the next round.

---

## 🎮 Control Scheme

The battleground is split down the middle. Master your side of the board:

| Actions | 🕹️ Left Side: Black Starship | 🕹️ Right Side: Orange Starship |
| :--- | :--- | :--- |
| **Move Up** | <kbd>W</kbd> | <kbd>▲ Up Arrow</kbd> |
| **Move Down** | <kbd>S</kbd> | <kbd>▼ Down Arrow</kbd> |
| **Move Left** | <kbd>A</kbd> | <kbd>◀ Left Arrow</kbd> |
| **Move Right** | <kbd>D</kbd> | <kbd>▶ Right Arrow</kbd> |
| **Fire Laser** | <kbd>Left Ctrl</kbd> | <kbd>Right Ctrl</kbd> |

---

## 🛠️ Installation & Setup

### 1. Prerequisites
Ensure you have **Python 3.8 or higher** installed on your operating system.

### 2. Install Dependencies
Install the required Pygame framework via pip:
```bash
pip install pygame
```

### 3. File Architecture
To initialize the engine successfully, construct your local project directory to exactly match the structure below:

```text
├── your_game_script.py
└── Assets/
    ├── black_spaceship.png   # Left player sprite
    ├── orange_spaceship.png  # Right player sprite
    ├── Grenade.mp3           # Impact sound effect
    └── GunSilencer.mp3       # Firing sound effect
```

---

## 🏃 Combat Rules & Deployment

Launch the battle system directly from your terminal:
```bash
python your_game_script.py
```

* **Hull Integrity:** Both combatants deploy with **10 Health Points**.
* **Weapon Limits:** Weapon cooling systems restrict players to a maximum of **3 active projectiles** on screen at once.
* **Victory Condition:** The first starship to hit **0 Health Points** suffers critical failure. The surviving player is crowned winner, and the system resets after a 3-second delay.

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.
