# 🐍 Classic Snake Game in Python

A classic, object-oriented implementation of the retro Snake game built using Python's built-in `turtle` graphics module. This project was developed as part of a Python programming journey to practice Object-Oriented Programming (OOP) principles, modular code architecture, and game loops.

---

## 🕹️ Features

* **Object-Oriented Design**: Cleanly separated into modular classes (`Snake`, `Food`, and `Score`) following proper encapsulation and inheritance.
* **Smooth Controls**: Responsive arrow key bindings (`Up`, `Down`, `Left`, `Right`) with built-in logic preventing the snake from instantly reversing into itself.
* **Dynamic Scoring**: Score tracking that updates live on the screen every time the snake successfully consumes food.
* **Collision Detection**: 
  * Wall collision detection to trigger a "Game Over" state.
  * Self-collision detection preventing the snake from running into its own body segments.
* **Procedural Growth**: The snake dynamically extends its length whenever it eats food.

---

## 📂 Project Structure

```text
├── main.py       # Core game loop, screen setup, and collision management
├── snake.py      # Snake class managing movement, body segments, and controls
├── food.py       # Food class handling random spawning and refreshing
└── score.py      # Score class handling text rendering, score tracking, and game over screens
