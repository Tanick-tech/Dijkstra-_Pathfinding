import pygame as pg



# Window's measurement
window_width = 500
window_height = 500
# Creating the window's interface
window = pg.display.set_mode((window_width, window_height))
# Creating columns and rows
columns = 25
rows = 25
box_width = window_width // columns
box_height = window_height // rows
# Creating an empty grid as a list
queue = []
path = []
grid = []