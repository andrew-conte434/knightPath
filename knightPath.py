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

for r in range(8):
    row = []
    for c in range(8):
        row.insert(0, count)
        count -= 1
    grid.append(row)
    

class Node:
    def __init__(self, square, dist=0):
        self.square = square
        self.dist = dist
        
    def __hash__(self):
        return hash(self.square, self.dist)
    
    def __eq__(self, other):
        return (self.square, self.dist) == (other.square, other.dist)




    
def getLegalMoves(grid, x, y):
    moves = []
    #defines coordinates of all possible knight moves in clockwise order
    movesX = [1, 2, 2, 1, -1, -2, -2, -1]
    movesY = [2, 1, -1, -2, -2, -1, 1, 2]
    
    for i in range(8):
        if 0 <= x + movesX[i - 1] <= 7 and 0 <= y + movesY[i - 1] <= 7: 
            moves.append(grid[x + movesX[i-1]][y + movesY[i-1]])
    
    return moves


def getCoordinates(square, grid):
    for i, subList in enumerate(grid):
        if square in subList:
            return [i, subList.index(square)]

        
        
def bfs(start, end, grid):
    
    queue = []
    visited = []
    
    root = Node(start)
    dest = Node(end)
    
    queue.append(root)
    
    while queue:
        
        node = queue.pop(0)
        
        if node.square == dest.square:
            return node.dist
        
        if node not in visited:
            visited.append(node)
            
            coordinates = getCoordinates(node.square, grid)
            moves = getLegalMoves(grid, coordinates[0], coordinates[1])
            
            for i in moves:
                queue.append(Node(i, node.dist + 1))
    
for row in grid:
    print(row)
    
start = input("Enter starting square: ")
end = input("Enter ending square: ")

def checkInput(start, end, grid):
    if not start.isnumeric() or not end.isnumeric():
        print("Invalid input!")
        return
    start = int(start)
    end = int(end)
    if not start in range(0, 64) or not end in range(0, 64):
        print("Invalid input!")
        return
    print("Distance: ",bfs(start, end, grid))




checkInput(start, end, grid)
