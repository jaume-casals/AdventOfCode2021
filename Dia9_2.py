from collections import deque as queue

f = open("Input9.txt")

inp = f.readlines()

f.close()

row = []
matrix = []
for line in inp:
    for c in line.rstrip("\n"):
        row.append(int(c))
    matrix.append(row)
    row = []

height = len(matrix)
width = len(matrix[0])
lows = []

dRow = [ -1, 0, 1, 0]
dCol = [ 0, 1, 0, -1]
 
# Function to check if a cell
# is be visited or not
def isValid(vis, row, col, x, y):
   
    # If cell lies out of bounds
    if (row < 0 or col < 0 or row >= height or col >= width):
        return False
 
    # If cell is already visited
    if (vis[row][col]):
        return False
    if (matrix[row][col] == 9):
        return False
    if (matrix[row][col] <= matrix[x][y]):
        return False
 
    # Otherwise
    return True
 

def BFS(grid, vis, row, col):
   
    # Stores indices of the matrix cells
    q = queue()
    count = 0
 
    # Mark the starting cell as visited
    # and push it into the queue
    q.append(( row, col ))
    vis[row][col] = True
 
    # Iterate while the queue
    # is not empty
    while (len(q) > 0):
        cell = q.popleft()
        x = cell[0]
        y = cell[1]
 
        #q.pop()
 
        # Go to the adjacent cells
        for i in range(4):
            adjx = x + dRow[i]
            adjy = y + dCol[i]
            if (isValid(vis, adjx, adjy, x, y)):
                q.append((adjx, adjy))
                vis[adjx][adjy] = True
                count += 1
    return count
 


for x in range(height):
    for y in range(width):
        curr = matrix[x][y]
        top = (x == 0)
        bottom = (x == height-1)
        left = (y == 0)
        right = (y == width-1)
        if not top and (matrix[x-1][y] > curr):
            top = True
        if not bottom and (matrix[x+1][y] > curr):
            bottom = True
        if not left and (matrix[x][y-1] > curr):
            left = True
        if not right and (matrix[x][y+1] > curr):
            right = True

        if top and bottom and left and right:
            lows.append((x, y))
            
results = []
vis = [[False for i in range(width)] for j in range(height)]

for l in lows:
    results.append(BFS(matrix, vis, l[0], l[1]))

result = 1
results = sorted(results, reverse = True)[:3]
for r in results:
    result = result * (r+1)
print("result:", result)
