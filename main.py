
def pirntGrid(Grid):
    row = len(Grid)
    col = len(Grid[0])

    for x in range(row):
        for y in range(col):
            print (lastG[x][y],end = ''),
        print("")







lastG = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
pirntGrid(lastG)
