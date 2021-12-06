f = open("Input6.txt")

inp = f.readline()

f.close()

inp = inp.split(',')

l = [int(x) for x in inp]
for i in range(80):
    s = len(l)
    for x in range(s):
        if l[x] > 0:
            l[x] -= 1
        else:
            l[x] = 6
            l.append(8)

print("count:", len(l))