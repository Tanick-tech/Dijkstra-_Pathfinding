import pygame as pg
from settings import *

# This class comprises all the different types of cells, boxes in the grid
class Box:
    def __init__(self,i, j):
        self.x = i
        self.y = j
        self.start = False
        self.wall = False
        self.target = False
        self.queued = False
        self.visited = False
        self.neighbors = []
        self.prior = None
        '''
        These "Falses" mark as flags for each of the variables.
        Whereas
        '''
    def draw(self,win, color):
        pg.draw.rect(win,color, (self.x * box_width, self.y * box_height, box_width - 2, box_height - 2)) # He said is about some sort of margin or something
    def set_neighbour(self): # This code will handle the upcoming blocks which is stored in a list
        if self.x > 0:
            self.neighbors.append(grid[self.x - 1][self.y])
        if self.x < columns - 1:
            self.neighbors.append(grid[self.x + 1][self.y])
        if self.y > 0:
            self.neighbors.append(grid[self.x][self.y - 1])
        if self.y < rows - 1:
            self.neighbors.append(grid[self.x][self.y + 1])
        '''
        The first 2 if are to set the neighboring blocks into a list (called neighbors)
        The next 2 if are to set the neighboring blocks into a list (called neighbors)
        '''

