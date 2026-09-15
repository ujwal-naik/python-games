# 🚀 Space Dodge

[![Python Version](https://shields.io)](https://python.org)
[![Pygame](https://shields.io)](https://pygame.org)
[![License: MIT](https://shields.io)](https://opensource.org)

A fast-paced, 2D arcade survival game built using **Python** and **Pygame**. Take control of your starship, navigate a hazardous space arena, and dodge a relentless barrage of falling meteors. 

The longer you survive, the faster and more chaotic space becomes. **How long can you last?**

---

## ✨ Features

*   🕹️ **Dual Control Layout** – Full support for both standard Arrow keys and WASD layouts.
*   📈 **Dynamic Difficulty** – Asteroid spawn rates and falling speeds scale automatically over time to keep you on your toes.
*   🛡️ **Bulletproof Architecture** – Built using a robust state management machine rather than recursive loops, ensuring crash-free, infinite restarts.
*   🏁 **Game-Over Analytics** – Displays your exact final survival time down to the millisecond with instant hotkeys to replay or exit.

---

## 🕹️ Controls

| Action | Primary Key | Alternative Key |
| :--- | :---: | :---: |
| **Move Left** | `←` Left Arrow | `A` |
| **Move Right** | `→` Right Arrow | `D` |
| **Move Up** | `↑` Up Arrow | `W` |
| **Move Down** | `↓` Down Arrow | `S` |
| **Retry** *(Game Over)* | `R` | — |
| **Quit** *(Game Over)* | `Q` | — |

---

## 📂 File Structure

```text
├── space_dodge/
│   ├── main.py          # Main application loop & state machine logic
│   └── space bg.jpg     # Background graphic (Automatic fallback included)
└── README.md            # Project documentation
```

---

## 🛠️ Prerequisites & Installation

### 1. Clone the Repository
```bash
git clone https://github.com
cd space-dodge
```

### 2. Verify Python Installation
Ensure you have **Python 3.7 or higher** installed:
```bash
python --version
```

### 3. Install Dependencies
Install the required **Pygame** library via pip:
```bash
pip install pygame
```

---

## 🚀 How to Run

Launch the game by running the main Python script from your terminal:
```bash
python main.py
```

---

## 📝 License

This project is open-source and available under the [MIT License](LICENSE). Feel free to fork, modify, and use it for personal learning and development.
