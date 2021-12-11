f = open("Input10.txt")

inp = f.readlines()

f.close()

tancat = [')', ']', '}', '>']
obert = ['(', '[', '{', '<']
score = [3, 57, 1197, 25137]


def puntuacio(c):
    for i in range(len(tancat)):
        if c == tancat[i] or c == obert[i]:
            return score[i]
    x = 6/0 # No hauria de passar :)

def tanquen(p1, p2):
    for i in range(len(tancat)):
        if p1 == obert[i] and p2 == tancat[i]:
            return True
    return False

def invers(c):
    for i in range (len(tancat)):
        if c == tancat[i]:
            return obert[i]
        elif c == obert[i]:
            return tancat[i]
    print("NOOOOOOOOOOO")
    return "XXXXXXXXXXX"

def canvStr(s, pos, c):
    return s[:pos] + c + s[pos + 1:]

def buscaObert(ant, l, corr):
    i = ant
    found = False
    while not found:
        found = l[i] in obert and not corr[i]
        if not found:
            i -= 1
    return i

def rec(i, l):
    correcte = [False for i in range(len(l))]
    ant = i
    punt = 0
    li = (l+".")[:-1]
    for x in range(len(l)):
        if l[x] in obert:
            ant = x
        else:
            if not tanquen(l[ant], l[x]):
                punt += puntuacio(l[x])
            correcte[ant] = True
            correcte[x] = True

            ant = buscaObert(ant, l, correcte)
    return punt


def punts(l):
    sum = 0
    i = 0
    found = False
    while not found and i < len(l):
        if l[i] in obert:
            found = True
        else:
            print("letsgo")
            sum += puntuacio(l[i])
            i = i+1;
    sum += rec(i, l)
    return sum


sum = 0
for l in inp:
    sum += punts(l.rstrip("\n"))

print("sum:", sum)