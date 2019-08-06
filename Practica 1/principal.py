# Clear the screen and hold it for 3 seconds
import curses
import time
from curses import KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN

stdscr = curses.initscr() #initialize console
height = 20
width = 60
h, w = stdscr.getmaxyx()
pos_y = 0
pos_x = 0
window = curses.newwin(height, width, pos_x, pos_y) #create a new window
window.keypad(True) #enable keypad mode
curses.noecho() #prevent input from displaying in the screen
curses.curs_set(0) #cursor invisible (0)
window.border(0) #default border for our window
window.nodelay(True) #return -1 when no key is pressed

key = KEY_RIGHT
pos_x = 5
pos_y = 5
window.addch(pos_y, pos_x, '*')
#run program while [ESC] key is not pressed
while key != 27:
    window.timeout(100)
    keystroke = window.getch()
    if keystroke is not -1:
        key = keystroke
    window.addch(pos_y, pos_x, ' ') #erase last dot
    if key == KEY_RIGHT:
        pos_x = pos_x + 1
    elif key == KEY_LEFT:
        pos_x = pos_x - 1
    elif key == KEY_UP:
        pos_y = pos_y - 1
    elif key == KEY_DOWN:
        pos_y = pos_y + 1
    window.addch(pos_y, pos_x, '*')

curses.endwin()
