import string
import csv

## files csv test. uncomment only one
#input = 'oscillators.csv'
input = 'space_ships.csv'
#input = 'still_lifes.csv'
#input = 'test.csv'


w, h = 27, 27
matrix = [["-" for x in range(w)] for y in range(h)] 
matrix_temp = [["-" for x in range(w)] for y in range(h)] 

inicio, fin = 1, 26

def copyMatrix():
    for x in range(inicio,fin):
        for y in range(inicio,fin):
            matrix_temp[y][x] = matrix[y][x]



def initMatrixFromCSV(matrix):
    with open(input, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            matrix[int(row[1]) +1 ][int(row[0]) +1 ] = "x"

def updateMatrix(matrix):
    copyMatrix()

    for x in range(inicio,fin):
        for y in range(inicio,fin):
            if matrix[y][x] ==  "-":
                matrix[y][x] = born(matrix,x,y)
            else:
                matrix[y][x] = dead(matrix,x,y)
   
def getPerimeter(matrix,x,y):
    count = 0

    for i in range(x -1,x + 2):
        for u in range(y -1,y + 2):
                if matrix_temp[u][i] == "x":
                    if not (i == x and u == y):
                        count = count +1
    
    return count

def born(matrix,x,y):
    neighbors = getPerimeter(matrix,x,y)

    ## only if have 3 neightbors born
    if neighbors == 3:
        return "x"
    else:
        return "-"

def dead(matrix,x,y):
    neighbors = getPerimeter(matrix,x,y)

    ## less than 2 neightborns deads
    if neighbors < 2:
        return "-"
    ## only if it have 2 or 3 neighbors lives
    elif neighbors == 2 or neighbors == 3:
        return "x"
    # if it have more than 3 neighbors deads
    elif neighbors > 3:
        return "-"


def showMatrix(matrix, stdscr):
    stdscr.clear()
    for col in range(inicio,fin):
        for row in range(inicio,fin):
            result = str(matrix[row][col])
            stdscr.addstr(row, col, result)
    stdscr.refresh()
    
    
