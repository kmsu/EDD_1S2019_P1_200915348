import curses
import csv
import os.path
from users import circular
from users import node
usersList = circular()

menu = ["Home", "Play", "Scoreboard", "User selection", "Reports", "Bulk loading", "Exit"]
submenu = ["Yes", "No"]

def print_menu(stdscr, selected_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    for idx, row in enumerate(menu): #enumerate retorna en idx la posicion y en row el texto en esa posicion
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row) #add text to show
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()

def print_sub_menu(stdscr, selected_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    for idx, row in enumerate(submenu): #enumerate retorna en idx la posicion y en row el texto en esa posicion
        x = w//2 - len(row)//2 + (idx*(len(row)+2))
        y = h//2 - len(menu)//2
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row) #add text to show
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()

def print_center(stdscr, text):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    x = w//2 - len(text)//2
    y = h//2
    stdscr.addstr(y, x, text)
    stdscr.refresh()

def main(stdscr):
    # turn off cursor blinking
    curses.curs_set(0)
    # color scheme for selected row
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    # specify the current selected row
    current_row = 0
    # print the menu
    print_menu(stdscr, current_row)

    nodeUser = usersList.getHead()
    while 1:
        key = stdscr.getch()
        #nodeUser = usersList.getHead()
        #user = nodeUser
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
            print_menu(stdscr, current_row)
        elif key == curses.KEY_DOWN and current_row < len(menu)-1:
            current_row += 1
            print_menu(stdscr, current_row)
        elif key == curses.KEY_ENTER or key in [10, 13]:
            #print_center(stdscr, "You selected '{}'".format(menu[current_row]))
            #stdscr.getch()
            if current_row == 0:
                print_center(stdscr, "regresar a home")
                #print_sub_menu(stdscr, 0)
            elif current_row == 1:
                print_center(stdscr, "iniciar juego")
            elif current_row == 2:
                print_center(stdscr, "Scoreboard")
            elif current_row == 3:
                print_center(stdscr, "user selection")
                nodeUser = usersList.getHead()
                if nodeUser is None:
                    print_center(stdscr, "users not found")
                else:
                    print_center(stdscr, nodeUser.data)
                    
            elif current_row == 4:
                print_center(stdscr, "Reports")
            elif current_row == 5:
                print_center(stdscr, "Bulk loading")
                usersList.archivo()
                #usersList.print_list()
            # if user selected last row, exit the program
            elif current_row == len(menu)-1:
                print_center(stdscr, "finalizar juego")
                break
            else:
                print_menu(stdscr, current_row)

        elif key == curses.KEY_LEFT:
            user = nodeUser.previous
            print_center(stdscr, user.data)
            nodeUser = user
        elif key == curses.KEY_RIGHT:
            user = nodeUser.next
            print_center(stdscr, user.data)
            nodeUser = user

curses.wrapper(main)
