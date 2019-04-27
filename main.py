
def pirntGrid(Grid):
    row = len(Grid)
    col = len(Grid[0])

    for x in range(row):
        for y in range(col):
            print (Grid[x][y],end = ''),
        print("")



def sumCell(Grid,x,y):
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

def Generate(Grid):
    row = len(Grid)
    col = len(Grid[0])
    temp = [[0 for i in range(col)] for j in range (row)]

    for x in range(row):
        for y in range(col):
            sum = sumCell(Grid,x,y)
           
            #when itself is alive
            if Grid[x][y] == 1:
                # case when it die
                if sum <= 1 or sum >= 4:
                    temp[x][y] = 0
                else:
                    temp[x][y] = 1
            #when itslef is died
            else:
                if sum == 3:
                    temp[x][y] = 1
                else:
                    temp[x][y] = 0
            
            return temp




print("first")
First = [[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1]]
pirntGrid(First)
print("second")
second = Generate(First)
pirntGrid(second)



