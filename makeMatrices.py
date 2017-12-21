def makeMatrix(size, start, doIncrement):
    a = []
	
    num = start
    
    for x in range(size):
        a.append([])
        
    for x in range(size):
        for y in range(size):
            a[x].append(num)
            if doIncrement:
                num += 1
    return a
	
def printMatrix(matrix):
    a = matrix

    for x in range(len(a)):
        for y in range(len(a[x])):
            print(a[x][y], end='\t')
        print()

def upperL():
    a = makeMatrix(4, 0, False)
    num = 1
    
    for x in range(len(a)):
        for y in range(len(a)):
            if x == 0:
                a[x][y] = num
                num += 1
            else:
                a[x][len(a)-1] = num
                num += 1
                break
    return a


printMatrix(upperL())
