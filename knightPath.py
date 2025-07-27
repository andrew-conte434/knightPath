"""

This program will use a breadth-first search to find the shortest path for a 
knight to move between two squares on a chessboard. 
"""

class Node:
    def __init__(self, square, parent = None, dist=0):
        self.square = square
        self.parent = parent
        self.dist = dist

        
    def __hash__(self):
        return hash(self.square, self.parent, self.dist)
    
    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        else:
            return (self.square, self.parent, self.dist) == (other.square, other.parent, other.dist)


def main():

    grid = generateGrid()

    for row in grid:
        print(row)
    
    start = input("Enter starting square: ")
    end = input("Enter ending square: ")

    if checkInput(start, end) == False:
        print("Invalid input!")
    else:
        result = bfs(int(start), int(end), grid)
        printResult(result)
    


def generateGrid():
    
    grid = []
    count = 63

    for r in range(8):

        row = []

        for c in range(8):
            row.insert(0, count)
            count -= 1
            
        grid.insert(0, row)
    
    return grid

      
def checkInput(start, end) -> bool:
    if not start.isnumeric() or not end.isnumeric():
        return False
    
    start = int(start)
    end = int(end)

    if not start in range(0, 64) or not end in range(0, 64):
        return False
    
    return True

     
def bfs(start, end, grid):
    
    queue = []
    visited = []
    
    root = Node(start)
    dest = Node(end)
    
    queue.append(root)
    
    while queue:
        
        node = queue.pop(0)
        
        if node.square == dest.square:
            return node
        
        if node not in visited:
            visited.append(node)
            
            coordinates = [node.square // 8, node.square % 8]
            moves = getLegalMoves(grid, coordinates[0], coordinates[1])
            
            for i in moves:
                queue.append(Node(i, node, node.dist + 1))


# Returns a list of all legal moves from a given position on the grid 
def getLegalMoves(grid, x, y):
    moves = []
    #defines coordinates of all possible knight moves in clockwise order
    movesX = [1, 2, 2, 1, -1, -2, -2, -1]
    movesY = [2, 1, -1, -2, -2, -1, 1, 2]
    
    for i in range(8):
        if 0 <= x + movesX[i - 1] <= 7 and 0 <= y + movesY[i - 1] <= 7: 
            moves.append(grid[x + movesX[i-1]][y + movesY[i-1]])
    
    return moves

def printResult(finalNode):
    nodesVisited = []

    node = finalNode
    
    # Populate path list, using 'while True' because python doesn't have do..while loops  
    while True:
        nodesVisited.insert(0, node.square)
        if node.parent == None:
            break
        else:
            node = node.parent

    path = nodesVisited[0] if len(nodesVisited) == 1 else " -> ".join(map(str, nodesVisited))
    
    print("DISTANCE: ", finalNode.dist)
    print("PATH: ", path)


if __name__ == "__main__":
    main()

