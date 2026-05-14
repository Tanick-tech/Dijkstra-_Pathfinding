# Dijkstra Pathfinding in Python

Credit: **Max Rohowsky**
Tutorial: https://www.youtube.com/watch?v=QNpUN8gBeLY

This repository aims to reconstruct the Dijkstra pathfinding algorithm using Python as an introductory project for high-school students to become familiar with pathfinding concepts and algorithm visualization.

The project demonstrates how shortest-path searching works through an interactive grid-based visualization, helping students understand algorithmic thinking, graph traversal, and real-time graphical feedback using pygame.

---

## Tech Stack

* Python
* Pygame
* Tkinter

---

## Highlight Features

### 1. Introduction to Tkinter

This project introduces the use of the tkinter library for graphical user interface interactions such as pop-up messages and user notifications.

While tkinter is used for message dialogs, the main visualization and interactive grid system are entirely handled by pygame.

### 2. Dijkstra Pathfinding Algorithm

The pathfinding logic is implemented using a queue-based search system.

Each grid cell tracks:

* Its neighboring cells
* Whether it is a wall
* Whether it has been visited
* Whether it has been queued for exploration

The visualization uses different colors to clearly display the algorithm’s progress in real time.

The algorithm explores cells step by step until it reaches the target node, then reconstructs the shortest path by backtracking through stored prior connections.

### 3. Interactive Visualization

Users can:

* Place walls and obstacles
* Define start and target nodes
* Watch the search process unfold visually
* Observe how the shortest path is reconstructed

This provides a more intuitive understanding of pathfinding behavior compared to static textbook examples.

---

## Directory Structure

```bash id="kpjlwm"
Dijkstra-_Pathfinding/
│
├── Code/
│   ├── box.py
│   ├── main.py
│   └── settings.py
│
├── .gitignore
├── LICENSE
└── README.md
```

### Important Files

* `main.py` starts the visualization and handles the main program loop
* `box.py` defines the grid cells and their behaviors during the pathfinding process
* `settings.py` stores constants and configuration values used throughout the project

---

## Run Locally

Clone the repository:

```bash id="l3y4jh"
git clone <your-repository-link>
```

Go to the project directory:

```bash id="1jlwmf"
cd Dijkstra-_Pathfinding
```

Install dependencies:

```bash id="4pc0nl"
pip install pygame
```

Run the program:

```bash id="d6sqin"
python Code/main.py
```

---

## Conclusion

This project successfully demonstrates an interactive pathfinding visualizer built with pygame.

It allows users to create obstacles, define targets, and observe the pathfinding process in real time through graphical feedback.

The program helps students:

* Understand the fundamentals of Dijkstra pathfinding
* Learn grid-based traversal logic
* Explore algorithm visualization techniques
* Gain experience working with pygame and tkinter
* Strengthen problem-solving and computational thinking skills

Overall, this repository serves as both an educational tool and a practical introduction to pathfinding algorithms in Computer Science.
