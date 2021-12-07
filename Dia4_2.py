f = open("Input4.txt")

num = [int(x) for x in f.readline().split(',')]

f.readline()
x=0
matrix=[]
row = []
for line in f:
    line = line.strip("\n")
    if line == "":
        matrix.append(row)
        row = []
    else:
        row.append([int(x) for x in line.split()])

if (len(row) > 0):
    matrix.append(row)

f.close()

def puntuacio(ind, num):
    mat = matrix[ind]
    bmat = bLines[ind]
    sum = 0
    for l in range(len(mat)):
        for x in range(len(mat[l])):
            if not bmat[l][x]:
                sum += mat[l][x]
    return sum*num

def hiHaLin(mat, i, j):
    trobat = True
    for x in mat[i]:
        if not x:
            trobat = False
            break
    if trobat:
       return True
    trobat = True
    for x in mat:
        if not x[j]:
            trobat = False
            break
    return trobat

def elementInsertat(m, x, ind):
    for l in range(len(m)):
        for i in range(len(m[l])):
            if m[l][i] == x:
                bLines[ind][l][i] = True
                return hiHaLin(bLines[ind], l, i)


w, h = len(matrix[0][0]), len(matrix[0])
bLines = [[[False for x in range(w)] for y in range(h)] for i in range(len(matrix))]
guanyat = [False for i in range(len(matrix))]
puntuation = 0

for x in num:
    if puntuation > 0:
        break
    for m in range(len(matrix)):
        b = elementInsertat(matrix[m], x, m)
        if b: #La matriu fa bingo
            guanyat[m] = True
            if guanyat.count(False) == 0:
                print(matrix[m], x)
                puntuation = puntuacio(m, x)
                break

    if puntuation > 0:
        break

print("puntuacio:", puntuation)

