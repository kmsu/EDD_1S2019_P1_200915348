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
#pos_y = 0
#pos_x = 0
window = curses.newwin(height, width, 0, 0) #create a new window
window.keypad(True) #enable keypad mode
curses.noecho() #prevent input from displaying in the screen
curses.curs_set(0) #cursor invisible (0)
window.border(0) #default border for our window
window.nodelay(True) #return -1 when no key is pressed

key = KEY_RIGHT
#pos_x = 1
#pos_y = 1

snake.startSnake()
nodeHeadSnake = snake.getHead()
nodeTailSnake = snake.getLast()

x_coordinate = random.randint(1,58)
y_coordinate = random.randint(1,18)
type = random.randint(0,100)
type_food = 0

if type <= 20:
    type_food = 0 #bocadillo malo
    window.addch(y_coordinate, x_coordinate, '*')
else:
    type_food = 1 #bocadillo bueno
    window.addch(y_coordinate, x_coordinate, '+')

#show the first snake
aux = nodeHeadSnake
while aux.next is not None:
    window.addch(aux.data_y, aux.data_x, '#')
    aux = aux.next
window.addch(aux.data_y, aux.data_x, '#')

#aux = nodeTailSnake
#while aux.previous is not None:
#    window.addch(aux.data_y, aux.data_x, '#')
#    aux = aux.previous
#window.addch(aux.data_y, aux.data_x, '#')

#run program while [ESC] key is not pressed
while key != 27:
    window.timeout(10000)
    keystroke = window.getch()
    if keystroke is not -1:
        key = keystroke
    #window.addch(pos_y, pos_x, ' ') #erase last dot

#-----------------------------------------------new coordinates---------------------------------------
    if key == KEY_RIGHT:
        #pintar los nodos desde la cola en la posicion de su anterior
        temp = snake.getLast()
        window.addch(temp.data_y, temp.data_x, ' ')
        while temp.previous is not None:
            #aux = temp.next
            temp.data_y = temp.previous.data_y
            temp.data_x = temp.previous.data_x
            window.addch(temp.data_y, temp.data_x, '#')
            temp = temp.previous
        #cambia la posicion de la cabeza
        temp.data_x = temp.data_x + 1
        window.addch(temp.data_y, temp.data_x, '#')

        #verifica si la cabeza esta sobre una comida
        if snake.getHead().data_x == x_coordinate and snake.getHead().data_y == y_coordinate:
            if type_food == 1:
                snake.addList(int(x_coordinate), int(y_coordinate))
            else:
                window.addch(snake.getLast().data_y, snake.getLast().data_x, ' ') #elimina la cola
                snake.delete() #elimina el nodo cola de la lista

            #genera un nuevo bocadillo
            x_coordinate = random.randint(1,58)
            y_coordinate = random.randint(1,18)
            type = random.randint(0,100)
            type_food = 0

            if type <= 20:
                type_food = 0 #bocadillo malo
                window.addch(y_coordinate, x_coordinate, '*')
            else:
                type_food = 1 #bocadillo bueno
                window.addch(y_coordinate, x_coordinate, '+')


        #pos_x = pos_x + 1
    elif key == KEY_LEFT:
        temp = snake.getLast()
        window.addch(temp.data_y, temp.data_x, ' ')
        while temp.previous is not None:
            #aux = temp.next
            temp.data_y = temp.previous.data_y
            temp.data_x = temp.previous.data_x
            window.addch(temp.data_y, temp.data_x, '#')
            temp = temp.previous
        temp.data_x = temp.data_x - 1
        window.addch(temp.data_y, temp.data_x, '#')

        if snake.getHead().data_x == x_coordinate and snake.getHead().data_y == y_coordinate:
            if type_food == 1:
                #print("coordenada x comida" + str(x_coordinate), end = " ")
                #print("coordenada y comida" + str(y_coordinate), end = " ")
                #print(" ")
                snake.addList(int(x_coordinate), int(y_coordinate))
                #snake.print_list()
            else:
                window.addch(snake.getLast().data_y, snake.getLast().data_x, ' ')
                snake.delete()
            x_coordinate = random.randint(1,58)
            y_coordinate = random.randint(1,18)
            type = random.randint(0,100)
            type_food = 0

            if type <= 20:
                type_food = 0 #bocadillo malo
                window.addch(y_coordinate, x_coordinate, '*')
            else:
                type_food = 1 #bocadillo bueno
                window.addch(y_coordinate, x_coordinate, '+')

        #pos_x = pos_x - 1
    elif key == KEY_UP:
        temp = snake.getLast()
        window.addch(temp.data_y, temp.data_x, ' ')
        while temp.previous is not None:
            #aux = temp.next
            temp.data_y = temp.previous.data_y
            temp.data_x = temp.previous.data_x
            window.addch(temp.data_y, temp.data_x, '#')
            temp = temp.previous
        temp.data_y = temp.data_y - 1
        window.addch(temp.data_y, temp.data_x, '#')

        if snake.getHead().data_x == x_coordinate and snake.getHead().data_y == y_coordinate:
            if type_food == 1:
                #print("coordenada x comida" + str(x_coordinate), end = " ")
                #print("coordenada y comida" + str(y_coordinate), end = " ")
                #print(" ")
                snake.addList(int(x_coordinate), int(y_coordinate - 1))
                #snake.print_list()
            else:
                window.addch(snake.getLast().data_y, snake.getLast().data_x, ' ')
                snake.delete()
            x_coordinate = random.randint(1,58)
            y_coordinate = random.randint(1,18)
            type = random.randint(0,100)
            type_food = 0

            if type <= 20:
                type_food = 0 #bocadillo malo
                window.addch(y_coordinate, x_coordinate, '*')
            else:
                type_food = 1 #bocadillo bueno
                window.addch(y_coordinate, x_coordinate, '+')
        #pos_y = pos_y - 1

    elif key == KEY_DOWN:
        temp = snake.getLast()
        window.addch(temp.data_y, temp.data_x, ' ')
        while temp.previous is not None:
            #aux = temp.next
            temp.data_y = temp.previous.data_y
            temp.data_x = temp.previous.data_x
            window.addch(temp.data_y, temp.data_x, '#')
            temp = temp.previous
        temp.data_y = temp.data_y + 1
        window.addch(temp.data_y, temp.data_x, '#')

        if snake.getHead().data_x == x_coordinate and snake.getHead().data_y == y_coordinate:
            if type_food == 1:
                #print("coordenada x comida " + str(x_coordinate), end = " ")
                #print(" coordenada y comida " + str(y_coordinate))
                #print(" ")
                snake.addList(int(x_coordinate), int(y_coordinate))
                #snake.print_list()
            else:
                window.addch(snake.getLast().data_y, snake.getLast().data_x, ' ')
                snake.delete()
            x_coordinate = random.randint(1,58)
            y_coordinate = random.randint(1,18)
            type = random.randint(0,100)
            type_food = 0

            if type <= 20:
                type_food = 0 #bocadillo malo
                window.addch(y_coordinate, x_coordinate, '*')
            else:
                type_food = 1 #bocadillo bueno
                window.addch(y_coordinate, x_coordinate, '+')
        #pos_y = pos_y + 1

#----------------------------------avoid the snake die when touch the walls------------------------
# evita que la snake muera en las paredes y aparezca en el lado contrario
    val = snake.getHead()
    if(val.data_x > 58):
        window.addch(val.data_y, val.data_x, ' ')
        val.data_x = 1
        window.addch(val.data_y, val.data_x, '#')
    elif(val.data_x < 1):
        window.addstr(val.data_y, val.data_x, ' ')
        val.data_x = 58
        window.addch(val.data_y, val.data_x, '#')
        #pos_x = 58
        #window.addstr(pos_y, pos_x, '#')
    elif(val.data_y > 18):
        window.addstr(val.data_y, val.data_x, ' ')
        val.data_y = 1
        window.addch(val.data_y, val.data_x, '#')
        #pos_y = 1
        #window.addstr(pos_y, pos_x, '#')
    elif(val.data_y < 1):
        window.addstr(val.data_y, val.data_x, ' ')
        val.data_y = 18
        window.addch(val.data_y, val.data_x, '#')
        #pos_y = 18
curses.endwin()
