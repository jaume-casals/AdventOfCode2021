from copy import deepcopy
f = open("Input3.txt")

inp = f.readlines()

f.close()

size = len(inp[0])

def mostCommon(s, lis):
    num0 = 0
    num1 = 0
    for l in lis:
        if l[s] == '0':
            num0 += 1;
        else:
            num1 += 1;
    if (num1 >= num0):
        return "1"
    else:
        return "0"


lOx = deepcopy(inp)

for s in range(0, size-1):
    mc = mostCommon(s, lOx)
    for l in inp:
        if l in lOx:
            if len(lOx) == 1:
                break
            if l[s] != mc:
                lOx.remove(l)
    if len(lOx) == 1:
        break

lco2 = deepcopy(inp)

for s in range(0, size-1):
    mc = mostCommon(s, lco2)
    for l in inp:
        if l in lco2:
            if len(lco2) == 1:
                break
            if l[s] == mc:
                lco2.remove(l)
    if len(lco2) == 1:
        break


print("Oxygen:", lOx[0], "\tCO2:", lco2[0])
print("Multiplication:", int(lOx[0], 2)*int(lco2[0], 2))
