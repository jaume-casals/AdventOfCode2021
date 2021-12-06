f = open("Input6.txt")

inp = f.readline()

f.close()

inp = inp.split(',')

l = [int(x) for x in inp]
dies = [0 for x in range(9)]

for x in l:
    dies[x] += 1


count = len(l)

for i in range(256):
    count += dies[0]
    aux = dies[0]
    for i in range(8):
        dies[i] = dies[i+1]
    dies[8] = aux
    dies[6] += aux

print("count:", count)