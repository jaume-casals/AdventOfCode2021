f = open('Input1.txt', 'r')

inp = f.readlines()

f.close()

ant = int(inp[0]) + int(inp[1]) + int(inp[2])
count = 0
start = 3
while start < len(inp):
    if int(inp[start])+int(inp[start-1])+int(inp[start-2]) > int(ant):
        count += 1
    ant -= int(inp[start-3])
    ant += int(inp[start])
    start += 1

print(count)