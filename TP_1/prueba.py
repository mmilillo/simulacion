
import time
import curses

curses.LINES = 30
curses.COLS = 30

#inicializa curses
stdscr = curses.initscr()

#oculta el cursor
curses.curs_set(False)

def probar(stdscr):

    #no espera la resppuesta del usuario
    stdscr.nodelay(True)

    c = -1
    i = 0
    while c != ord('q'):
        c = stdscr.getch()
        ##aca imprimiria matriz
        stdscr.addstr(1, i, ".")
        stdscr.refresh()
        time.sleep(1) 
        i = i+1


    

##le manda por defecto un parametro de la libreria curses inicializado
##curses.wrapper(probar)
