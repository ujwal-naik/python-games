# Simple 2-Player Space Shooter

A classic **2-player arcade game** built in Python using the `pygame` library. Two players control spaceships (Black and Orange) on opposite sides of the screen, maneuvering to dodge incoming lasers while trying to deplete the opponent's health.

## 🚀 Features

* **Local Multiplayer:** Simultaneous 2-player action on a single keyboard.
* **Border Constraints:** A central boundary restricts spaceships to their respective halves of the arena.
* **Dynamic Health Tracking:** Both players start with 10 health points, tracked via an on-screen display.
* **Audio Feedback:** Custom sound effects play when firing lasers or successfully hitting an opponent.
* **Game Loop Reset:** The game automatically restarts after declaring a winner.

---

## 🎮 Controls

### 🕹️ Left Side: Black Spaceship
* **Move Up:** `W`
* **Move Down:** `S`
* **Move Left:** `A`
* **Move Right:** `D`
* **Shoot Laser:** Left Control (`LCTRL`)

### 🕹️ Right Side: Orange Spaceship
* **Move Up:** `Up Arrow`
* **Move Down:** `Down Arrow`
* **Move Left:** `Left Arrow`
* **Move Right:** `Right Arrow`
* **Shoot Laser:** Right Control (`RCTRL`)

---

## 🛠️ Requirements & Installation

### 1. Prerequisites
Make sure you have **Python 3.x** installed on your system.

### 2. Install Pygame
Install the Pygame library using pip:
```bash
pip install pygame
```

### 3. Asset Directory Structure
Before launching the game, ensure your project directory has an `Assets` folder containing the required audio and image files:
```text
├── your_game_script.py
└── Assets/
    ├── black_spaceship.png
    ├── orange_spaceship.png
    ├── Grenade.mp3          (Hit sound effect)
    └── GunSilencer.mp3      (Firing sound effect)
```

---

## 🏃 How to Play

1. Run the Python script from your terminal:
   ```bash
   python your_game_script.py
   ```
2. Each player starts with **10 Health**.
3. Fire at your opponent while avoiding their shots. Maximum of 3 bullets per player can be on screen at a time.
4. The first player to reach **0 Health** loses, and the winner is announced on screen.
