f = open("Input11.txt")

inp = f.readlines()

f.close()

def suma1casella(x, y, matrix):
    if matrix[x][y] > 0:
        matrix[x][y] = matrix[x][y]+1
        if matrix[x][y] == 10:
            matrix[x][y] = 0
            return 1
    return 0

def suma1local(x, y, matrix):
    flash = 0
    height = len(matrix)
    width = len(matrix[0])

    top = (x == 0)
    bottom = (x == height-1)
    left = (y == 0)
    right = (y == width-1)

    if not top:
        flash += suma1casella(x-1, y, matrix)
    if not bottom:
        flash += suma1casella(x+1, y, matrix)
    if not left:
        flash += suma1casella(x, y-1, matrix)
    if not right:
        flash += suma1casella(x, y+1, matrix)
    if not top and not right:
        flash += suma1casella(x-1, y+1, matrix)
    if not top and not left:
        flash += suma1casella(x-1, y-1, matrix)
    if not bottom and not right:
        flash += suma1casella(x+1, y+1, matrix)
    if not bottom and not left:
        flash += suma1casella(x+1, y-1, matrix)
    return flash

def newFlashes(matrix, flashed):
    flash = 0
    for i in range(len(matrix)):  
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0 and not flashed[i][j]:
                flashed[i][j] = True
                flash += suma1local(i, j, matrix)
    return flash

def suma1(matrix):
    flash = 0
    for i in range(len(matrix)):  
        for j in range(len(matrix[0])):
            matrix[i][j] = matrix[i][j] + 1
            if matrix[i][j] == 10:
                matrix[i][j] = 0
                flash += 1
    return flash

matrix = []

for line in inp:
    matrix.append([int(x) for x in list(line.rstrip("\n"))])

flash = 0

for iter in range(100):
    flashed = [[False for i in range(len(matrix))] for j in range(len(matrix[0]))]
    flash += suma1(matrix)
    newFlash = -1
    while (newFlash) != 0:
        if (newFlash != 0): newFlash = 0
        newFlash = newFlashes(matrix, flashed)
        flash += newFlash


for x in matrix:
    print(x)
print("flashes:", flash)