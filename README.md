# Dijkstra Pathfinding in Python

Credit by: ***Max Rohowsky*** (link: https://www.youtube.com/watch?v=QNpUN8gBeLY )
This repository aims to reconstruct Dijkstra pathfinding method using Python as an introductory project to a high-school student
to get familiar with this pathfinding method. It is one of the fundamental algorithm to prepare for their pursuit 
of Computer Science major career path.

## Instructions
Clone the repository: 

Install dependencies (if any):

Run the game: python main.py
## Highlight Features

#### 1. **The introduction to tkinter**
This code is mainly run of tkinter library. This is used to pop-up messages (when the code can't find a solution to the problem) and GUI window (means interacting with the users). However, the visualization is handled entirely by Pygame.
#### 2. **The Algorithm**
The pathfinding logic is implemented with a queue-based search.
Each box tracks its neighbors, whether it's a wall, visited or queued (the visualization colors make the algorithm's progess clear). 
The algorithm explores cells step by step until it reaches the target, then reconstructs the path by backtracking through the prior links.
## Conclusion
This program successfully demonstrates an **interactive pathfinding visualizer** built with Pygame. It allows users to set walls, define a target, and watch the search unfold in real time. The algorithm explores the grid step by step, marking visited and queued cells, and reconstructs the path once the target is reached.  
Although Tkinter is imported, the visualization and interaction are handled entirely by Pygame. 
In short, the code provides a solid foundation for learning and visualizing pathfinding, combining interactive controls with clear graphical feedback.

 