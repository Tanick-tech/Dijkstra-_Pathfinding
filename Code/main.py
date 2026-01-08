from tkinter import messagebox, Tk
import pygame as pg
import sys
from settings import *
from box import *

# Creating Grid
for i in range (columns):
    arr =[]
    for j in range (rows):
        arr.append(Box(i, j))
    grid.append(arr)
start_box = grid[0][0]
start_box.start = True # The indicator to show the starting box opened

# Set neighbours:
for i in range(columns):
    for j in range(rows):
        grid[i][j].set_neighbour()

start_box = grid[0][0]
start_box.visited = True
start_box.queued = True
queue.append(start_box)

# The running code:
def main():
    # Conditions
    begin_search = False
    target_box_set = False
    searching = True
    target_box = None
    while True:
        for event in pg.event.get():
            # Quit window
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            # Mouse controls
            elif event.type == pg.MOUSEMOTION: # Must have motion in order to set up the 'final destination cell'
                x = pg.mouse.get_pos()[0] # The right click of the mouse
                y = pg.mouse.get_pos()[1] # The left click of the mouse
                # Draw wall
                if event.buttons[0]:
                    i = x // box_width
                    j = y // box_height
                    grid[i][j].wall = True
                # Set target
                if event.buttons[2] and not target_box_set: #event,button[2] means right click
                    i = x // box_width
                    j = y // box_height
                    target_box = grid[i][j]
                    target_box.target = True
                    target_box_set = True
            # Start Algorithm
            if event.type == pg.KEYDOWN and target_box_set: # Press 1 random key on the keyboard then the algorithm runs
                begin_search = True
        if begin_search:
            if len(queue) > 0 and searching:
                current_box = queue.pop(0)
                current_box.visited = True
                if current_box == target_box:
                    searching = False
                    while current_box.prior != start_box:
                        path.append(current_box.prior)
                        current_box = current_box.prior
                else:
                    for neighbour in current_box.neighbors:
                        if not neighbour.queued and not neighbour.wall:
                            neighbour.queued = True
                            neighbour.prior = current_box
                            queue.append(neighbour)

            '''
            The idea of this is DFS (depth first search)
            All the box is queued, after searching for the possibility by setting the neighbouring cells, it is contained in the queue (the rest is popped)
            DFS is used to find the shortest possible way to get the final destination box.
            '''


        # All the drawings take action
        window.fill((0,0,0))
        for i in range(columns):
            for j in range(rows):
                box = grid[i][j]
                box.draw(window, (50, 50, 50))
                if box.queued:
                    box.draw(window, (200, 0, 0))
                if box.visited:
                    box.draw(window, (0, 200, 0))
                if box in path:
                    box.draw(window, (0, 0, 200))
                if box.wall:
                    box.draw(window, (90, 90, 90))
                if box.start:
                    box.draw(window, (0, 200, 200))
                if box.target:
                    box.draw(window, (200, 200, 0))






        pg.display.flip() # Similar to pg.display.update()

main() # The code finally runs
