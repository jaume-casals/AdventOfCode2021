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

sum = 0
height = len(matrix)
width = len(matrix[0])

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
            sum += curr+1
print(sum)
    
