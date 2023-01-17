# import time
import curses

# to get curses for windows.
#python -m pip install windows-curses

def list_taker(a_list):
    global the_list
    the_list = a_list
    # print(the_list)

def menu_printer(stdscr,the_row_number,the_list):
    #this function prints the option list and highlights the row passed to it.
    
    stdscr.clear() # this clears the screen.
    curses.init_pair(1,curses.COLOR_RED, curses.COLOR_WHITE)
    #it creates a color pair for highlighting. This is pair 1. You can have more.
    
    for index,items in enumerate(the_list):
        stdscr.addstr(index,0,items)
        if index==the_row_number:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(index,0,items)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(index,0,items)


    stdscr.refresh()
    

def item_selector(stdscr):
    curses.curs_set(0)  #this stops the cursor from blinking
    current_row = 0
    menu_printer(stdscr,current_row,the_list)
    
    while 1: # this creates an infinite while loop.my_the_list, the_list
        
            
        key = stdscr.getch() # this will capture the key stroke on the screen.
        stdscr.clear() # this will simply clear the screen from any output from the last loop run.

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1     
        # stdscr.addstr(0,0,"you pressed UP arrow key!")
        elif key == curses.KEY_DOWN and current_row < len(the_list)-1:
            current_row += 1

        elif (key == curses.KEY_ENTER or key in [10,13]):
            stdscr.addstr(0,0,f"you pressed {the_list[current_row]}")
            stdscr.refresh()
            stdscr.getch()
            return the_list[current_row]
            break

        elif (key == curses.KEY_ENTER or key in [10,13]) and current_row == len(the_list)-1 :
            stdscr.addstr(0,0,"you pressed ENTER to Exit!, press any key to exit")
            stdscr.refresh()
            stdscr.getch()
            break
        
        
        menu_printer(stdscr,current_row,the_list)
        stdscr.refresh() # this is required for you to see whats written on screen

def list_printer(the_list):
    for items in the_list:
        print (items)

# test=curses.wrapper(main)
# # print(f"your choice was {test}")
# curses.wrapper(item_selector)