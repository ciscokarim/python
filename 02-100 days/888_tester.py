import pyautogui
import time

def no_lock(button):
    try:
        print ('Press CTRL+C to stop.')
        while True:
            pyautogui.press(button)     # Key pressed
            time.sleep(2)

    except Exception as ex:
        print ('no_lock | Error: ', ex)

def main():
    try:
        print ('\nPrevent Windows screenlock')
        kb_button = str(input('Enter keyboard button: '))
        
        print ('\nRunning')
        no_lock(kb_button)

    except KeyboardInterrupt:
        print('\nStopped')

    except Exception as ex:
        print ('main | Error: ', ex)

if __name__ == "__main__":
    main()
    
#  print("one")
# print("two")
# print("three")
# for i in range(1,4):
#     print(i)
# print("four")
# print("five")


# mylist=["a","b","c"]


# # find the index "b"
# charloc = mylist.index("b")
  
# # replace "b" with "k" by slicing the list and adding k in the middle.
# mylist = mylist[:charloc]+["k"]+mylist[charloc+1:]

# # # find the index of Rahul
# # i = l.index('Rahul')
  
# # # replace Rahul with Shikhar
# # l = l[:i]+['Shikhar']+l[i+1:]
# print(mylist)