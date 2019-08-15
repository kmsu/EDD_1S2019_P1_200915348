import curses
import csv
import os.path
import sys
import random
import time

from users import circular
from users import node
from snake import doubleLinkedList
from score import pila
from scoreboard import queue

userList = circular()
nodeUser = node()
snake = doubleLinkedList()
score = pila()
Scoreboard = queue()

#for exit of game  without saving the actual game pres end key

menu = ["Play", "Scoreboard", "User selection", "Reports", "Bulk loading", "Exit"]
menuReport = ["Users", "Snake Report","Score Report", "scoreboard Report"]
#user_in_game = None

def paint_title(win,var):
    win.clear()                         #it's important to clear the screen because of new functionality everytime we call this function
    win.border(0)                       #after clearing the screen we need to repaint the border to keep track of our working area
    x_start = round((60-len(var))/2)    #center the new title to be painted
    win.addstr(0,x_start,var)

#paint for the snake not erase the window when cross the walls
def paint_title_game(win, var, score_game, user):
    win.border(0)
    x_start = round((60-len(var))/2)
    win.addstr(0,x_start,var)
    show = "score: " + str(score_game)
    win.addstr(0,0, show)
    x = round((60-len(user)))
    win.addstr(0, x, user)
#def paint_score(win, score_game):
#    #win.border(0)
#    show = "score: " + str(score_game)
#    win.addstr(0,0, show)

def paint_menu(win, selected_row_idx):
    paint_title(win,' MAIN MENU ')   #paint title
    for idx, row in enumerate(menu): #enumerate retorna en idx la posicion y en row el texto en esa posicion
        x = round((60-len(row))/2)
        y = 20//2 - len(menu)//2 + idx
        if idx == selected_row_idx:
            win.attron(curses.color_pair(1))
            win.addstr(y, x, row)
            win.attroff(curses.color_pair(1))
        else:
            win.addstr(y, x, row)

def paint_menu_report(win, selected_row_idx_report):
    paint_title(win,' REPORTS ')          #paint title
    for idx, row in enumerate(menuReport): #enumerate retorna en idx la posicion y en row el texto en esa posicion
        x = round((60-len(row))/2)
        y = 20//2 - len(menuReport)//2 + idx
        if idx == selected_row_idx_report:
            win.attron(curses.color_pair(1))
            win.addstr(y, x, row)
            win.attroff(curses.color_pair(1))
        else:
            win.addstr(y, x, row)


def print_center(win, text):
    #win.clear()
    #paint_title(win, text)
    x = 60//2 - len(text)//2
    y = 20//2
    win.addstr(y, x, text)
    win.refresh()

def print_user(win, text, varTitle):
    paint_title(win, varTitle)
    x = 60//2 - len(text)//2
    y = 20//2
    win.addstr(y, x, text)
    win.refresh()

def food(win):
    global x_coordinate
    global y_coordinate
    global type_food
    global type

    x_coordinate = random.randint(1,58)
    y_coordinate = random.randint(1,18)
    type = random.randint(0,100)
    if type <= 20:
        type_food = 0
        win.addch(y_coordinate, x_coordinate, '*') #decrease the snake
    else:
        type_food = 1
        win.addch(y_coordinate, x_coordinate, '+')#increases the snake

def snakeSize(win):
    global x_coordinate
    global y_coordinate
    global type_food
    global score_game

    #verifica si la cabeza esta sobre una comida
    if snake.getHead().data_x == x_coordinate and snake.getHead().data_y == y_coordinate:

        if type_food == 1:
            snake.addList(int(x_coordinate), int(y_coordinate))
            score.push(x_coordinate, y_coordinate)
            score_game = score_game + 1
        else:
            if snake.sizeSnake() > 3:
                win.addch(snake.getLast().data_y, snake.getLast().data_x, ' ') #elimina la cola
                snake.delete() #elimina el nodo cola de la lista
                score.pop()
                score_game = score_game - 1

        x_coordinate = random.randint(1,58)
        y_coordinate = random.randint(1,18)
        type = random.randint(0,100)
        if type <= 20:
            type_food = 0
            win.addch(y_coordinate, x_coordinate, '*') #decrease the snake
        else:
            type_food = 1
            win.addch(y_coordinate, x_coordinate, '+')#increases the snake

def main(stdscr):
    curses.initscr()#initialize console
    curses.curs_set(0)
    height = 20
    width = 60
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.noecho()
    #variables of game
    user_in_game = None
    global score_game
    score_game = 0
    inGame = False # 0 = pay new game, 1 = continue last game
    level = 100
    #key = 0
    #variables of food
    type_food = 0
    x_coordinate = 0
    y_coordinate = 0
    #principal menu
    current_row = 0 # index of principal menu
    current_row_report = 0 #index for report menu
    #window
    s = curses.newwin(height, width, 0, 0)#create new window
    s.border(0)
    s.keypad(True)
    paint_menu(s, current_row)

    while(True):
        key = s.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
            paint_menu(s, current_row)
        elif key == curses.KEY_DOWN and current_row < len(menu)-1:
            current_row += 1
            paint_menu(s, current_row)
        elif key == curses.KEY_ENTER or key in [10, 13]:

            #play game option
            if current_row == 0:
                paint_title(s, "Play")
                #paint_title_game(s, "Play", score_game)
                #paint_score(s, score_game)
                nameUser = userList.getHead()
                if user_in_game is None:
                    s.addstr(10,20, "write your name:")
                    curses.echo()
                    s.addstr(11,20, " "*20, curses.A_UNDERLINE)
                    user_in_game = s.getstr(11,20)
                    curses.noecho()
                    print_center(s, str(user_in_game))
                    #text = user_in_game.replace('\'', '')
                    userList.insertarNodo(str(user_in_game))
#-------------------------------------Juego---------------------------
                else:

                    s.nodelay(True)
                    key = curses.KEY_RIGHT
                    #start snake with size 3
                    if inGame == False:
                        snake.startSnake()
                        inGame = True
                        level = 100
                    #get head and tail of snake
                    nodeHeadSnake = snake.getHead()
                    nodeTailSnake = snake.getLast()
                    #generate the snack
                    food(s)
                    #show the first snake
                    aux = nodeHeadSnake
                    while aux.next is not None:
                        s.addch(aux.data_y, aux.data_x, '#')
                        aux = aux.next
                    s.addch(aux.data_y, aux.data_x, '#')
                    #run program while [ESC] key is not pressed
                    while key != 27:
                        s.timeout(level)#level es el valor que debe quedar
                        keystroke = s.getch()
                        if keystroke is not -1:
                            key = keystroke

#-----------------------------New coordinates---------------------------
                        #right direction
                        if key == curses.KEY_RIGHT:
                            #pintar los nodos desde la cola en la posicion de su anterior
                            temp = snake.getLast()
                            s.addch(temp.data_y, temp.data_x, ' ')
                            while temp.previous is not None:
                                #aux = temp.next
                                temp.data_y = temp.previous.data_y
                                temp.data_x = temp.previous.data_x
                                s.addch(temp.data_y, temp.data_x, '#')
                                temp = temp.previous
                            #cambia la posicion de la cabeza
                            temp.data_x = temp.data_x + 1
                            s.addch(temp.data_y, temp.data_x, '#')

#---------------------------verify if snake eats to self-------------------------------------------------------------------
                            stat = False
                            temp = snake.getHead().next
                            while temp is not None:
                                if snake.getHead().data_x == temp.data_x and snake.getHead().data_y == temp.data_y:
                                    stat = True
                                    break
                                temp = temp.next

#----------------------------add to Scoreboard------------------------------------------------------------------------
                            if stat == True:
                                if Scoreboard.queue_count() == 10:
                                    Scoreboard.dequeue()
                                    Scoreboard.enqueue(str(user_in_game), score_game)
                                else:
                                    Scoreboard.enqueue(str(user_in_game), score_game)
                                snake.snakeReport()
                                snake.clear_list()
                                score.clear_list()
                                score_game = 0
                                inGame = False
                                break

                            snakeSize(s) #verify if head is on snack and increases or decrease according to snack

                            #if snake.getHead().data_x ==  and snake.getHead().data_y == y_coordinate:

                        # left direction
                        elif key == curses.KEY_LEFT:
                            temp = snake.getLast()
                            s.addch(temp.data_y, temp.data_x, ' ')
                            while temp.previous is not None:
                                #aux = temp.next
                                temp.data_y = temp.previous.data_y
                                temp.data_x = temp.previous.data_x
                                s.addch(temp.data_y, temp.data_x, '#')
                                temp = temp.previous
                            temp.data_x = temp.data_x - 1
                            s.addch(temp.data_y, temp.data_x, '#')

#---------------------------verify if snake eats to self-------------------------------------------------------------------
                            stat = False
                            temp = snake.getHead().next
                            while temp is not None:
                                if snake.getHead().data_x == temp.data_x and snake.getHead().data_y == temp.data_y:
                                    stat = True
                                    break
                                temp = temp.next

#----------------------------add to Scoreboard------------------------------------------------------------------------
                            if stat == True:
                                if Scoreboard.queue_count() == 10:
                                    Scoreboard.dequeue()
                                    Scoreboard.enqueue(str(user_in_game), score_game)
                                else:
                                    Scoreboard.enqueue(str(user_in_game), score_game)
                                snake.snakeReport()
                                snake.clear_list()
                                score.clear_list()
                                score_game = 0
                                inGame = False
                                break

                            snakeSize(s)

                        #up direction
                        elif key == curses.KEY_UP:
                            temp = snake.getLast()
                            s.addch(temp.data_y, temp.data_x, ' ')
                            while temp.previous is not None:
                                #aux = temp.next
                                temp.data_y = temp.previous.data_y
                                temp.data_x = temp.previous.data_x
                                s.addch(temp.data_y, temp.data_x, '#')
                                temp = temp.previous
                            temp.data_y = temp.data_y - 1
                            s.addch(temp.data_y, temp.data_x, '#')

#---------------------------verify if snake eats to self-------------------------------------------------------------------
                            stat = False
                            temp = snake.getHead().next
                            while temp is not None:
                                if snake.getHead().data_x == temp.data_x and snake.getHead().data_y == temp.data_y:
                                    stat = True
                                    break
                                temp = temp.next

#----------------------------add to Scoreboard------------------------------------------------------------------------
                            if stat == True:
                                if Scoreboard.queue_count() == 10:
                                    Scoreboard.dequeue()
                                    Scoreboard.enqueue(str(user_in_game), score_game)
                                else:
                                    Scoreboard.enqueue(str(user_in_game), score_game)
                                snake.snakeReport()
                                snake.clear_list()
                                score.clear_list()
                                score_game = 0
                                inGame = False
                                break

                            snakeSize(s)

                        #down direction
                        elif key == curses.KEY_DOWN:
                            temp = snake.getLast()
                            s.addch(temp.data_y, temp.data_x, ' ')
                            while temp.previous is not None:
                                #aux = temp.next
                                temp.data_y = temp.previous.data_y
                                temp.data_x = temp.previous.data_x
                                s.addch(temp.data_y, temp.data_x, '#')
                                temp = temp.previous
                            temp.data_y = temp.data_y + 1
                            s.addch(temp.data_y, temp.data_x, '#')

#---------------------------verify if snake eats to self-------------------------------------------------------------------
                            stat = False
                            temp = snake.getHead().next
                            while temp is not None:
                                if snake.getHead().data_x == temp.data_x and snake.getHead().data_y == temp.data_y:
                                    stat = True
                                    break
                                temp = temp.next

#----------------------------add to Scoreboard------------------------------------------------------------------------
                            if stat == True:
                                if Scoreboard.queue_count() == 10:
                                    Scoreboard.dequeue()
                                    Scoreboard.enqueue(str(user_in_game), score_game)
                                else:
                                    Scoreboard.enqueue(str(user_in_game), score_game)
                                snake.snakeReport()
                                snake.clear_list()
                                score.clear_list()
                                score_game = 0
                                inGame = False
                                break

                            #increases or decrease the size of snake
                            snakeSize(s)

                        #exit without saving game
                        elif key == curses.KEY_END:
                            snake.clear_list()
                            score.clear_list()
                            score_game = 0
                            inGame = False
                            break

#--------------------------avoid the snake die whwen touch the walls--------
                        val = snake.getHead()
                        if(val.data_x > 58):
                            s.addch(val.data_y, val.data_x, ' ')
                            val.data_x = 1
                            s.addch(val.data_y, val.data_x, '#')
                            #paint_title_game(s, "Play", score_game)
                        elif(val.data_x < 1):
                            s.addstr(val.data_y, val.data_x, ' ')
                            val.data_x = 58
                            s.addch(val.data_y, val.data_x, '#')
                            #paint_title_game(s, "Play", score_game)
                        elif(val.data_y > 18):
                            s.addstr(val.data_y, val.data_x, ' ')
                            val.data_y = 1
                            s.addch(val.data_y, val.data_x, '#')
                            #paint_title_game(s, "Play", score_game)
                        elif(val.data_y < 1):
                            s.addstr(val.data_y, val.data_x, ' ')
                            val.data_y = 18
                            s.addch(val.data_y, val.data_x, '#')
                            #paint_title_game(s, "Play", score_game)

                        #paint_title_game(s, "play", str(score.count_list()))
                        paint_title_game(s, "play", str(score_game), str(user_in_game))

                        if score_game == 15:
                            score.clear_list()
                            level = 50

                    paint_menu(s, current_row)

            #Scoreboard
            elif current_row == 1:
                paint_title(s, "Scoreboard")
                if Scoreboard.getHead() is None:
                    x_pos = round((60-len("The Scoreboard is empty"))/2)
                    s.addstr(9, x_pos, "The Scoreboard is empty")
                else:
                    #index = 6
                    #y = 20//2 - len(Scoreboard.count_list())//2 + index - 1
                    #x = 20
                    y = 5
                    s.addstr(y, 20, "Name")
                    s.addstr(y, 30, "Score")
                    temp = Scoreboard.getHead()
                    while temp.next is not None:
                        #x = round((60-len(row))/2)
                        y += 1
                        s.addstr(y, 20, str(temp.data))
                        s.addstr(y, 30, str(temp.data2))
                        temp=temp.next
                    y += 1
                    s.addstr(y, 20, str(temp.data))
                    s.addstr(y, 30, str(temp.data2))

            #user selection
            elif current_row == 2:
                paint_title(s, "User selection")
                nodeUser = userList.getHead()
                if nodeUser is None:
                    print_center(s, "users not found")
                else:
                    print_center(s, "<- " + nodeUser.data + " ->")
                    while 1:
                        key = s.getch()
                        if key == curses.KEY_LEFT:
                            user = nodeUser.previous
                            print_user(s, "<- " + user.data + " ->", "User selection")
                            nodeUser = user
                        elif key == curses.KEY_RIGHT:
                            user = nodeUser.next
                            print_user(s, "<- " + user.data + " ->", "User selection")
                            nodeUser = user
                        elif key == curses.KEY_ENTER or key in [10, 13]:
                            if inGame == True:
                                pass
                                #paint_title(s, "user selection")
                                #s.addstr(10,10,"you can't select other user while play is in pause")
                            else:
                                user_in_game = nodeUser.data
                            break
                        elif key == 27:
                            break
                    paint_menu(s, current_row)

            #menu report
            elif current_row == 3:

                paint_menu_report(s, current_row_report)
                while(True):
                    key = s.getch()
                    if key == curses.KEY_UP and current_row_report > 0:
                        current_row_report -= 1
                        paint_menu_report(s, current_row_report)
                    elif key == curses.KEY_DOWN and current_row_report < len(menuReport)-1:
                        current_row_report += 1
                        paint_menu_report(s, current_row_report)
                    elif key == curses.KEY_ENTER or key in [10, 13]:
                        #users report
                        if current_row_report == 0:
                            paint_title(s, "users report")
                            node = userList.getHead()
                            if node is None:
                                print_center(s, "list empty")
                            else:
                                #Create report by graphiz
                                f = open('userList.dot', 'w')
                                f.write('digraph users{\n')
                                f.write('node [shape=record];\n')
                                f.write('rankdir=LR;\n')
                                temp=node
                                count = 0
                                while temp.next is not node:
                                    f.write('node{} [label=\"{}\"];\n'.format(count,temp.data))
                                    count += 1
                                    f.write('node{} -> node{};\n'.format(count-1, count))
                                    f.write('node{} -> node{};\n'.format(count, count-1))
                                    temp = temp.next
                                f.write('node{} [label = \"{}\"];\n'.format(count, temp.data))
                                f.write('node'+ str(count) + ' -> node0\n')
                                f.write('node0 -> node' + str(count) + '\n')
                                f.write('}')
                                f.close()
                                os.system('dot userList.dot -Tpng -o userList.png')
                                os.system('userList.png')
                                print_center(s, "user report created")

                        #Snake Report
                        if current_row_report == 1:
                            paint_title(s, "Snake Report")

                            node = snake.getHead()
                            if node is None:
                                print_center(s, "list empty")
                            else:
                                #Create report by graphiz
                                f = open('snakeList.dot', 'w')
                                f.write('digraph snake{\n')
                                f.write('node [shape=record];\n')
                                f.write('rankdir=LR;\n')
                                f.write('node0 -> nodei;')
                                f.write('nodei [label = "null"];')
                                #temp=node
                                count = 0
                                #print(str(node.data_x))
                                #print(str(node.data_y))
                                while node.next is not None:
                                    f.write('node{} [label=\"{}\"];\n'.format(count, "(" + str(node.data_x) + "," + str(node.data_y) + ")"))
                                    count += 1
                                    f.write('node{} -> node{};\n'.format(count-1, count))
                                    f.write('node{} -> node{};\n'.format(count, count-1))
                                    node = node.next
                                f.write('node{} [label = \"{}\"];\n'.format(count, "(" + str(node.data_x) + "," + str(node.data_y) + ")"))
                                f.write('nodef [label = "null"];')
                                f.write('node'+ str(count) + ' -> nodef;\n')
                                f.write('}')
                                f.close()
                                os.system('dot snakeList.dot -Tpng -o snakeList.png')
                                os.system('snakeList.png')
                                print_center(s, "user report created")

                        #Score Report
                        if current_row_report == 2:
                            paint_title(s, "Score Report")

                            node = score.getHead()
                            if node is None:
                                print_center(s, "list empty")
                            else:
                                #Create report by graphiz
                                f = open('scoreList.dot', 'w')
                                f.write('digraph users{\n')
                                f.write('node [shape=record];\n')
                                f.write('rankdir=LR;\n')
                                f.write('struct [label = \" ')
                                #temp=node
                                count = 0
                                while node.next is not None:
                                    f.write('{}'.format(" |["+str(node.data_x)+","+str(node.data_y)+"]"))
                                    node = node.next
                                f.write('{}'.format(" |["+str(node.data_x)+","+str(node.data_y)+"]\" ];\n"))
                                f.write('}')
                                f.close()
                                os.system('dot scoreList.dot -Tpng -o scoreList.png')
                                os.system('scoreList.png')
                                print_center(s, "score report created")

                        #Scoreboard Report
                        if current_row_report == 3:
                            paint_title(s, "Scoreboard Report")

                            node = Scoreboard.getHead()
                            if node is None:
                                print_center(s, "list empty")
                            else:
                                #Create report by graphiz
                                f = open('scoreboardList.dot', 'w')
                                f.write('digraph scoreboard{\n')
                                f.write('node [shape=record];\n')
                                f.write('rankdir=LR;\n')
                                #temp=node
                                count = 0
                                while node.next is not None:
                                    f.write('node{} [label=\"{}\"];\n'.format(count, "(" + str(node.data) + "," + str(node.data2) + ")"))
                                    count += 1
                                    f.write('node{} -> node{};\n'.format(count-1, count))
                                    node = node.next
                                f.write('node{} [label = \"{}\"];\n'.format(count, "(" + str(node.data) + "," + str(node.data2) + ")"))
                                f.write('nodef [label = "null"];')
                                f.write('node'+ str(count) + ' -> nodef;\n')
                                f.write('}')
                                f.close()
                                os.system('dot scoreboardList.dot -Tpng -o scoreboardList.png')
                                os.system('scoreboardList.png')
                                print_center(s, "user report created")
                    elif key == 27:
                        paint_menu(s, current_row)
                        break
                    s.refresh()

            #bulk loading
            elif current_row == 4:
                paint_title(s, "Bulk loading")
                s.addstr(9, 20, "File: ")
                curses.echo()
                s.addstr(9, 26, " "*12, curses.A_UNDERLINE)
                nameFile = s.getstr(9,26)
                curses.noecho()
                try:
                    userList.archivo(nameFile)
                    s.clear()
                    paint_title(s, "Bulk loading")
                    print_center(s, "data loaded successfully")
                    key = s.getch()
                    if key == 27:
                        paint_menu(s, current_row)
                    #activar si debe regresar al menu para cargar otro archivo
                    #elif key == curses.KEY_ENTER or key in [10, 13]:
                    #    paint_menu(s, current_row)
                except:
                    print_center(s, "Error whit your file")


            elif key == curses.KEY_ENTER or key in [10, 13] and current_row == len(menu)-1:
                #exit()
                #print('exit')
                break

        s.refresh()
    curses.endwin()

curses.wrapper(main)
