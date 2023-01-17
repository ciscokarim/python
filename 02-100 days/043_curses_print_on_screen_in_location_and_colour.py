import time
import curses

# to get curses for windows.
#python -m pip install windows-curses

def main(stdscr):
    curses.curs_set(0)  #this stops the cursor from blinking
    h, w = stdscr.getmaxyx()  #this gets the max height and length of the screen for you.
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_WHITE)
    text1 = "Hello, how are you"
    # x = w//2 - len(text//2)
    # y = h//2
    text2=(f"height is {h} and width is {w}")
    
    x=0
    y=0
    stdscr.attron(curses.color_pair(1))
    stdscr.addstr(y, x, text1) # this adds the string in text1 to the specified location on the screen

    x=0
    y=1
    stdscr.attron(curses.color_pair(2))
    stdscr.addstr(y, x, text2) # this adds the string in text1 to the specified location on the screen

    stdscr.refresh() # screen has to be refreshed for the text screen to show up.
    time.sleep(5)


curses.wrapper(main)
