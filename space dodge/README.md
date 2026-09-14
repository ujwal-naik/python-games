# Space Dodge 🚀

A fast-paced, 2D arcade survival game built using **Python** and **Pygame**. Control your ship, navigate the space arena, and dodge a relentless barrage of falling stars for as long as possible. The longer you survive, the faster and more intense the game becomes!

## 🎮 Features
* **Dual Control Layout:** Support for both standard arrow keys and WASD layouts.
* **Dynamic Difficulty:** The spawn rate of the falling stars increases automatically over time.
* **Game-Over States:** View your final survival time with instant replay or quick-quit hotkeys.
* **Safe Architecture:** Uses a state management machine instead of recursion to prevent memory crashes on restarts.

---

## 🛠️ Prerequisites & Installation

### 1. Clone or Download the Project
Make sure all files (including your background images) are saved in the same directory.

### 2. Install Python
Ensure you have Python 3.7 or higher installed on your computer. You can check your version by running:
```bash
python --version
```

### 3. Install Pygame
Open your terminal or command prompt and install the Pygame dependency using pip:
```bash
pip install pygame
```

---

## 🚀 How to Run the Game

Navigate to your project folder using your terminal and run the main script file:

```bash
python main.py
```
*(Replace `main.py` with whatever you named your Python script file).*

---

## 🕹️ Controls

| Action | Primary Key | Alternative Key |
| :--- | :--- | :--- |
| **Move Left** | `← Left Arrow` | `A` |
| **Move Right** | `→ Right Arrow` | `D` |
| **Move Up** | `↑ Up Arrow` | `W` |
| **Move Down** | `↓ Down Arrow` | `S` |
| **Retry (Game Over)**| `R` | — |
| **Quit (Game Over)** | `Q` | — |

---

## 📂 File Structure

```text
├── space_dodge/
│   ├── main.py          # Main application code & game loops
│   └── space bg.jpg     # Required background graphic (Fallback included)
└── README.md            # Project documentation
```

---

## 📝 License
This project is open-source and free to use for personal learning and development.
