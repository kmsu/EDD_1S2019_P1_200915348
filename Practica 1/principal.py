# Clear the screen and hold it for 3 seconds
import curses
import time
import random

from curses import KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN
from snake import doubleLinkedList
snake = doubleLinkedList()

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
pos_x = 1
pos_y = 1

snake.startSnake()
nodeHeadSnake = snake.getHead()
nodeTailSnake = snake.getLast()

x_coordinate = random.randint(0,60)
y_coordinate = random.randint(0,20)
type = random.randint(0,100)

if type <= 20:
    type_food = 0 #bocadillo malo
    window.addch(y_coordinate, x_coordinate, '*')
else:
    type_food = 1 #bocadillo bueno
    window.addch(y_coordinate, x_coordinate, '+')

#aux = nodeHeadSnake
#while aux.next is not None:
#    window.addch(aux.data_y, aux.data_x, '#')
#    aux = aux.next
#window.addch(aux.data_y, aux.data_x, '#')

aux = nodeTailSnake
while aux.previous is not None:
    window.addch(aux.data_y, aux.data_x, '#')
    aux = aux.previous
window.addch(aux.data_y, aux.data_x, '#')

#run program while [ESC] key is not pressed
while key != 27:
    window.timeout(100000)
    keystroke = window.getch()
    if keystroke is not -1:
        key = keystroke
    #window.addch(pos_y, pos_x, ' ') #erase last dot

#-----------------------------------------------new coordinates---------------------------------------
    if key == KEY_RIGHT:
        #print("entre al if derecha")
        #obtener el ultimo nodo y poner la coordenad del nodo anterior
        temp = nodeTailSnake
        window.addch(temp.data_y, temp.data_x, ' ')
        while temp.previous is not None:
            #aux = temp.next
            temp.data_y = temp.previous.data_y
            temp.data_x = temp.previous.data_x
            window.addch(temp.data_y, temp.data_x, '#')
            temp = temp.previous
        temp.data_x = temp.data_x + 1
        window.addch(temp.data_y, temp.data_x, '#')
        if nodeHeadSnake.data_x == x_coordinate and nodeHeadSnake.data_y == y_coordinate:
            snake.addList(int(x_coordinate), int(y_coordinate))
            snake.print_list()

        #pos_x = pos_x + 1
    elif key == KEY_LEFT:
        temp = nodeTailSnake
        window.addch(temp.data_y, temp.data_x, ' ')
        while temp.previous is not None:
            #aux = temp.next
            temp.data_y = temp.previous.data_y
            temp.data_x = temp.previous.data_x
            window.addch(temp.data_y, temp.data_x, '#')
            temp = temp.previous
        temp.data_x = temp.data_x - 1
        window.addch(temp.data_y, temp.data_x, '#')
        if nodeHeadSnake.data_x == x_coordinate and nodeHeadSnake.data_y == y_coordinate:
            snake.addList(int(x_coordinate), int(y_coordinate))
            snake.print_list()

        #pos_x = pos_x - 1
    elif key == KEY_UP:
        temp = nodeTailSnake
        window.addch(temp.data_y, temp.data_x, ' ')
        while temp.previous is not None:
            #aux = temp.next
            temp.data_y = temp.previous.data_y
            temp.data_x = temp.previous.data_x
            window.addch(temp.data_y, temp.data_x, '#')
            temp = temp.previous
        temp.data_y = temp.data_y - 1
        window.addch(temp.data_y, temp.data_x, '#')
        if nodeHeadSnake.data_x == x_coordinate and nodeHeadSnake.data_y == y_coordinate:
            snake.addList(int(x_coordinate), int(y_coordinate))
            snake.print_list()
        #pos_y = pos_y - 1

    elif key == KEY_DOWN:
        temp = nodeTailSnake
        window.addch(temp.data_y, temp.data_x, ' ')
        while temp.previous is not None:
            #aux = temp.next
            temp.data_y = temp.previous.data_y
            temp.data_x = temp.previous.data_x
            window.addch(temp.data_y, temp.data_x, '#')
            temp = temp.previous
        temp.data_y = temp.data_y + 1
        window.addch(temp.data_y, temp.data_x, '#')
        if nodeHeadSnake.data_x == x_coordinate and nodeHeadSnake.data_y == y_coordinate:
            snake.addList(int(x_coordinate), int(y_coordinate))
            snake.print_list()
        #pos_y = pos_y + 1

#----------------------------------avoid the snake die when touch the walls------------------------
    print("este es x de head: " + str(nodeHeadSnake.data_x))
    print("este es y de head: " + str(nodeHeadSnake.data_y))
    print(" ")
    print("este es x: " + str(nodeTailSnake.data_x))
    print("este es y: " + str(nodeTailSnake.data_y))
    print(" ")
    if(int(nodeHeadSnake.data_x) > 58):
        window.addch(nodeTailSnake.data_y, nodeTailSnake.data_x, ' ')
        nodeTailSnake.data_x = 5

        window.addstr(10, 10, str(nodeTailSnake.data_x))

    elif(nodeTailSnake.data_x < 1):
        window.addstr(nodeHeadSnake.data_y, nodeHeadSnake.data_x, ' ')
        nodeTailSnake.data_x = 58
        #pos_x = 58
        #window.addstr(pos_y, pos_x, '#')
    elif(nodeTailSnake.data_y > 18):
        window.addstr(nodeHeadSnake.data_y, nodeHeadSnake.data_x, ' ')
        nodeTailSnake.data_y = 1
        #pos_y = 1
        #window.addstr(pos_y, pos_x, '#')
    elif(nodeTailSnake.data_y < 1):
        window.addstr(nodeHeadSnake.data_y, nodeHeadSnake.data_x, ' ')
        nodeTailSnake.data_y = 18
        #pos_y = 18
        #window.addstr(pos_y, pos_x, '#')

        #window.addch(temp.data_y, temp.data_x, ' ')


#-----------------------------paint------------------------------------------------------
    #while nodeHeadSnake.next is not None:
    #    window.addch(nodeHeadSnake.data_y, nodeHeadSnake.data_x, '#')
    #    nodeHeadSnake = nodeHeadSnake.next
    #    window.addch(nodeHeadSnake.data_y, nodeHeadSnake.data_x, '#')

    #window.refresh()




#curses.endwin()
