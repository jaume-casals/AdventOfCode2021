f = open("Input2.txt")

inp = f.readlines()

f.close()

x = 0
y = 0
aim = 0

for l in inp:
    op = l.split(" ",1)
    if (op[0] == "forward"):
        x += int(op[1])
        y += aim*int(op[1])
    elif (op[0] == "down"):
        aim += int(op[1])
    else:
       aim -= int(op[1])

print("x", x, "y", y)
print("x*y = ", x*y)