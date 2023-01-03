import random

#http://patorjk.com/software/taag/#p=display&v=0&f=Big&t=Can%20you%20Guess%3F%3F  
#above is where i got the following text converted from.

print('''
 _   _  _         _                                 _                                  
| | | |(_)       | |                               | |                                 
| |_| | _   __ _ | |__    ___  _ __    ___   _ __  | |      ___  __      __  ___  _ __ 
|  _  || | / _` || '_ \  / _ \| '__|  / _ \ | '__| | |     / _ \ \ \ /\ / / / _ \| '__|
| | | || || (_| || | | ||  __/| |    | (_) || |    | |____| (_) | \ V  V / |  __/| |   
\_| |_/|_| \__, ||_| |_| \___||_|     \___/ |_|    \_____/ \___/   \_/\_/   \___||_|   
            __/ |                                                                      
           |___/                                                                       
           
''')

def dictprinter(a_dict):
   for keys,values in a_dict.items():
      print(f"{keys}:{values}")

def answer_checker(a_random_key,a_response):
      
      if a_response==holdict[a_random_key]["answer"]:
         print("!!! Right Answer !!!")
         answer_is_right=True
         print(answer_is_right)
      else:
         print(" :(  Wrong Answer :( ")
         answer_is_right=False
         print(answer_is_right)
      
      return answer_is_right

holdict={
   
   1:{"statement":"Argentina won the world cup 3 times, Brazil won it more or less times? ","answer":"more"},
   2:{"statement":"Rihanna has 640aafdas00 followers, shakira has more or less followers? ","answer":"less"},
   3:{"statement":"Aftab has 612341234514000 followers, basit has more or less followers? ","answer":"more"},
   4:{"statement":"lalloo has 1232341341514 followers, balloo has more or less followers? ","answer":"more"},
   5:{"statement":"gsoga has 5321234112345131 followers, joga has more or less followers? ","answer":"less"},
   6:{"statement":"tisto has 5212623452342343 followers, mito has more or less followers? ","answer":"more"},
   7:{"statement":"jango has 775123412341154 followers, rango has more or less followers? ","answer":"less"},
   8:{"statement":"bakree has 7435123123132 followers, jakree has more or less followers ?","answer":"less"}
        
        }

# dictprinter(holdict)

holist=[1,2,3,4,5,6,7,8]

random.shuffle(holist)
# print(holist)

def gameplay():
   answer_is_right=True
   # while (answer_is_right==True):
   correct_counter=0
   for item in holist:

      # random_key=random.randint(1,8)
      # print(f"random_key={random_key}")
      # print(holdict[random_key]["statement"])
      qstring=holdict[item]["statement"]
      response=input(f"{qstring}")
      # print(f"response={response}")
      # print(f"answer_is_right before the change = {answer_is_right}")
      answer_is_right=answer_checker(item,response)
      if answer_is_right==True:
         correct_counter+=1
        
      if answer_is_right==False:
         print(f"Final score = {correct_counter}") 
         break
      
      print(f"Score so far = {correct_counter}")

gameplay()

