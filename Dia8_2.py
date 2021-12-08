f = open("Input8.txt")

inp = f.readlines()

f.close()

SevenSegments = [{str([True, True, True, False, True, True, True]): 0}, 
                {str([False, False, True, False, False, True, False]): 1},
                {str([True, False, True, True, True, False, True]): 2},
                {str([True, False, True, True, False, True, True]): 3},
                {str([False, True, True, True, False, True, False]): 4},
                {str([True, True, False, True, False, True, True]): 5},
                {str([True, True, False, True, True, True, True]): 6},
                {str([True, False, True, False, False, True, False]): 7},
                {str([True, True, True, True, True, True, True]): 8},
                {str([True, True, True, True, False, True, True]): 9}]

def decode(x, dicpi):
    on = [False for x in range(7)]
    for c in x:
        on[dicpi[c]] = True
    for j in SevenSegments:
        if str(on) in j.keys():
            return str(j[str(on)])
    

def dicti(code):
    dicpi = dict(((code[val], val) for val in range(len(code))))
    return dicpi

def conversio(num, code):
    res = ""
    for x in num:
        res = res + (decode(x, dicti(code)))
    return int(res)


sum = 0

for l in inp:
    result = ['X' for x in range(7)]
    lele = l.rstrip("\n").split('|')
    x = lele[0].split()
    partDarrere = lele[1].split()
    x = sorted(x, key=len)
    result[0] = (set(x[1]).difference(set(x[0]))).pop()

    pos = -1
    
    if (x[6].find(x[0][0]) == -1):
        pos = 6
        result[2] = x[0][0]
        result[5] = x[0][1]
    elif (x[6].find(x[0][1]) == -1):
        pos = 6
        result[2] = x[0][1]
        result[5] = x[0][0]
    elif (x[7].find(x[0][0]) == -1):
        pos = 7
        result[2] = x[0][0]
        result[5] = x[0][1]
    elif (x[7].find(x[0][1]) == -1):
        pos = 7
        result[2] = x[0][1]
        result[5] = x[0][0]
    elif (x[8].find(x[0][0]) == -1):
        pos = 8
        result[2] = x[0][0]
        result[5] = x[0][1]
    else:
        pos = 8
        result[2] = x[0][1]
        result[5] = x[0][0]

    i = 6
    q = 'X'
    y = 'X'
    se = set(x[9])
    o = set()
    while i < 9:
        if i != pos:
            o = o.union(se.difference(set(x[i])))
        i += 1
    q = o.pop()
    y = o.pop()
    
    finset = set(x[3])
    i = 4
    while i < 6:
        finset = finset.intersection(set(x[i]))
        i = i+1
    finset.remove(result[0])

    if q in finset:
        result[3] = q
        result[4] = y
        finset.remove(q)
    else:
        result[3] = y
        result[4] = q
        finset.remove(y)
    
    result[6] = finset.pop()
    result[1] = (set(x[2]).difference({result[2], result[3], result[5]})).pop()

    #ja tenim el codi a result[]
    sum += conversio(partDarrere, result)
    

print("sum of values:",sum)