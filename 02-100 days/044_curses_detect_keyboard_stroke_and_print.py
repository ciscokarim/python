import time
import curses

# to get curses for windows.
#python -m pip install windows-curses

def main(stdscr):
    curses.curs_set(0)  #this stops the cursor from blinking
    
    while 1: # this creates an infinite while loop.
        
        
        key = stdscr.getch() # this will capture the key stroke on the screen.
        stdscr.clear() # this will simply clear the screen from any output from the last loop run.

        if key == curses.KEY_UP:
            stdscr.addstr(0,0,"you pressed UP arrow key!")
        elif key == curses.KEY_DOWN:
            stdscr.addstr(0,0,"you pressed DOWN arrow key!")
        elif key == curses.KEY_LEFT:
            stdscr.addstr(0,0,"you pressed LEFT arrow key!")
        elif key == curses.KEY_RIGHT:
            stdscr.addstr(0,0,"you pressed RIGHT arrow key!")
        elif key == curses.KEY_ENTER or key in [10,13]:
            stdscr.addstr(0,0,"you pressed ENTER key!")

        stdscr.refresh() # this is required for you to see whats written on screen
        
curses.wrapper(main)
