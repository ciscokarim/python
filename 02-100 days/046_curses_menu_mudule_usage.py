import curses
from module_with_curses_menu_046 import *


mylist=["aftab","basit","munni","faizan","exit"]

for items in mylist:
    print (items)
# menu_printer("stdscr",3,mylist)

list_taker(mylist) ## pass the list
item_selected=curses.wrapper(item_selector) ## print the list and select the option.

print(item_selected)
