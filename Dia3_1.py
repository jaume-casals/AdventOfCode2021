f = open("Input3.txt")

inp = f.readlines()

f.close()

gamma = ""
epsilon = ""
size = len(inp[0])

for s in range(0, size-1):
    num0 = 0
    num1 = 0
    for l in inp:
        if l[s] == '0':
            num0 += 1;
        else:
            num1 += 1;
    
    if (num0 > num1):
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"

print("gamma:", gamma, "\tepsilon:", epsilon)
print("multiplication:", int(gamma, 2)*int(epsilon, 2))
