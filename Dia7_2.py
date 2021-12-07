f = open("Input7.txt")

inp = f.readline()

f.close()

inp = inp.split(',')

l = [int(x) for x in inp]

max = l[0]
min = l[0]

for x in l:
    if x > max:
        max = x
    if x < min:
        min = x

def fuel(l, pos):
    cost = 0
    for x in l:
        c = abs(x-pos)
        cost += int(c*(c+1)/2)
    return cost

m = 9999999999999999999999999999999999999
for i in range(min, max):
    y = fuel(l, i)
    if (y < m):
        m = y

print(m)