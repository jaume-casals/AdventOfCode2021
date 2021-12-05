from os import XATTR_SIZE_MAX


f = open("Input5.txt")

inp = f.readlines()

f.close()

xmax = 0
ymax = 0

i = []

for l in inp:
    x = l.split(' ')
    esq = x[0].split(',')
    dre = (x[2].split(','))
    dre[1] = dre[1].rstrip("\n")
    es = [0, 0]
    dr = [0, 0]
    es[0] = int(esq[0])
    es[1] = int(esq[1])
    dr[0] = int(dre[0])
    dr[1] = int(dre[1])

    i.append([es, dr])

l = []
for x in i:
    if (x[0][0] == x[1][0] or x[0][1] == x[1][1]):
        l.append(x)

for s in i:
    if max(s[0][0], s[1][0]) > xmax:
        xmax = max(s[0][0], s[1][0])

    if max(s[0][1], s[1][1]) > ymax:
        ymax = max(s[0][1], s[1][1])


matrix = [[0 for x in range(xmax+1)] for y in range(ymax+1)]

for x in l:
    itxIni = min(x[0][0], x[1][0])
    itxFin = max(x[0][0], x[1][0])
    if (itxIni != itxFin):
        while itxIni <= itxFin:
            matrix[x[0][1]][itxIni] += 1
            if (itxIni <= itxFin):
                itxIni += 1
            else:
                itxIni -= 1
    
    ityIni = min(x[0][1], x[1][1])
    ityFin = max(x[0][1], x[1][1])
    if (ityIni != ityFin):
        while ityIni <= ityFin:
            matrix[ityIni][x[0][0]] += 1
            if (ityIni <= ityFin):
                ityIni += 1
            else:
                ityIni -= 1

count = 0
for x in matrix:
    for p in x:
        if p > 1:
            count += 1

print("count:", count)