
def pirntGrid(Grid):
    row = len(Grid)
    col = len(Grid[0])

    for x in range(row):
        for y in range(col):
            print (lastG[x][y],end = ''),
        print("")



def sum(Grid,x,y):
    row = len(Grid)
    col = len(Grid[0])

    sum = 0

    for a in range(x-1,x+2):
        for b in range(y-1,y+2):
            if a<0 or a>row or b < 0 or b > col:
                continue
            elif a == x and b == y:
                continue
            else:
                sum = sum + Grid[a][b]
    
    return sum



lastG = [[0,1,0,0,0,0],[1,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
pirntGrid(lastG)
print(lastG[0][3])
print(sum(lastG,1,1))

