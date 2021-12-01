f = open('Input1.txt', 'r')

inp = f.readlines()

f.close()

ant = inp[0]
count = 0
start = 1
while start < len(inp):
    if int(inp[start]) > int(ant):
        count += 1
    ant = inp[start]
    start += 1

print(count)