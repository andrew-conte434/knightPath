# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""

This program will use a breadth-first search to find the shortest path for a 
knight to move between two squares on a chessboard. 
"""

grid = []
count = 63
square = 63

for r in range(8):
    row = []
    for c in range(8):
        row.insert(0, count)
        count -= 1
    grid.append(row)
    

def getCoordinates(sqaure, grid):
    for i, subList in enumerate(grid):
        if sqaure in subList:
            return [i, subList.index(square)]
    
def getLegalMoves(grid, square, x, y):
    moves = []
    
    #defines coordinates of all possible knight moves in clockwise order
    movesX = [1, 2, 2, 1, -1, -2, -2, -1]
    movesY = [2, 1, -1, -2, -2, -1, 1, 2]
    
    for i in range(8):
        if 0 <= x + movesX[i - 1] <= 7 and 0 <= y + movesY[i - 1] <= 7: 
            moves.append(grid[x + movesX[i-1]][y + movesY[i-1]])
    
    print(moves)
    
    return moves

def bfs(start, end):
    
    if start == end:
        return 0
    
    searchQueue = []
    auxQueue = []
    count = 1
    searchQueue.append(start)
    
    while true:
        searchQueue.extend(getLegalMoves(grid, start, x, y))
    
    
    
for row in grid:
    print(row)
    
startCoordinates = getCoordinates(square, grid)
getLegalMoves(grid, square, startCoordinates[0], startCoordinates[1])

