import curses
import csv
import os.path
from users import circular
from users import node
userList = circular()

menu = ["Play", "Scoreboard", "User selection", "Reports", "Bulk loading", "Exit"]
menuReport = ["Users", "Stack", "Queue"]
user_in_game = None

def paint_title(win,var):
    win.clear()                         #it's important to clear the screen because of new functionality everytime we call this function
    win.border(0)                       #after clearing the screen we need to repaint the border to keep track of our working area
    x_start = round((60-len(var))/2)    #center the new title to be painted
    win.addstr(0,x_start,var)

def paint_menu(win, selected_row_idx):
    paint_title(win,' MAIN MENU ')          #paint title
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

def main(stdscr):
    curses.initscr()
    curses.curs_set(0)
    height = 20
    width = 60
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.noecho()
    #key = 0
    current_row = 0
    current_row_report = 0
    s = curses.newwin(height, width, 0, 0)
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
            if current_row == 0:
                paint_title(s, "Play")
            elif current_row == 1:
                pass
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
                            user_in_game = nodeUser.data
                            break
                        elif key == 27:
                            break
                    paint_menu(s, current_row)
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
                    elif key == 27:
                        paint_menu(s, current_row)
                        break
                    s.refresh()
            elif current_row == 4:
                paint_title(s, "Bulk loading")
                
                print_center(s, "data loaded successfully")
                userList.archivo()
            elif key == curses.KEY_ENTER or key in [10, 13] and current_row == len(menu)-1:
                break

        s.refresh()
    curses.endwin()

curses.wrapper(main)
