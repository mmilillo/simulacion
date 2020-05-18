
import time
import curses
import prueba
import matrix_handler

#screen size
curses.LINES = 50
curses.COLS = 50

#inicialize curses
stdscra = curses.initscr()

#show curses
curses.curs_set(True)



def main(stdscr):
    prompt = "ingresa opcion: "

    # Clear screen
    stdscr.clear
    print(prompt)

    #y, x
    stdscr.move(0,len(prompt))


    c = stdscr.getkey()
    stdscr.move(1,1)
    if c == "b":
        matrix_handler.initMatrixFromCSV(matrix_handler.matrix)
        stdscr.nodelay(True)

        c = -1

        while c != ord('q'):
            c = stdscr.getch()
            matrix_handler.showMatrix(matrix_handler.matrix, stdscr)
            time.sleep(1)
            matrix_handler.updateMatrix(matrix_handler.matrix) 
            stdscr.refresh()
    elif c == "q":
        print("exit..")       


main(stdscra)
