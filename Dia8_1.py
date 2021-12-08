f = open("Input8.txt")

inp = f.readlines()

f.close()

count = 0

for l in inp:
    x = (((l.rstrip("\n")).split('|'))[1]).split()
    for t in x:
        if len(t) == 2 or len(t) == 3 or len(t) == 4 or len(t) == 7:
            count += 1
print(count)