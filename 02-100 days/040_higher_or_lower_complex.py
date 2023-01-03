import random
import os
# http://patorjk.com/software/taag/#p=display&v=0&f=Big&t=Can%20you%20Guess%3F%3F
# above is where i got the following text converted from.


holdict = {

    1: {"field": "singer", "name": "rihanna", "location": "usa", "followers": "123456134"},
    2: {"field": "player", "name": "messi", "location": "argentina", "followers": "835556134"},
    3: {"field": "singer", "name": "michale", "location": "usa", "followers": "613456134"},
    4: {"field": "player", "name": "ronaldo", "location": "portugal", "followers": "632156134"},
    5: {"field": "singer", "name": "sting", "location": "uk", "followers": "862156134"},
    6: {"field": "singer", "name": "jimmy", "location": "usa", "followers": "851256134"},
    7: {"field": "player", "name": "nemar", "location": "brazil", "followers": "732156134"},
    8: {"field": "actor", "name": "arnold", "location": "usa", "followers": "521256134"}

}


def title_printer():
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


def vs_printer():
    print('''       
 __      _______ 
 \ \    / / ____|
  \ \  / / (___  
   \ \/ / \___ \ 
    \  /  ____) |
     \/  |_____/ 
                 
     ''')


def dictprinter(a_dict):
    for keys, values in a_dict.items():
        print(f"{keys}:{values}")


def answer_checker(a_random_key, a_response):

    if a_response == holdict[a_random_key]["answer"]:
        print("!!! Right Answer !!!")
        answer_is_right = True
        print(answer_is_right)
    else:
        print(" :(  Wrong Answer :( ")
        answer_is_right = False
        print(answer_is_right)

    return answer_is_right


# =========================================================
# 0: Print the game title
# =========================================================
os.system("cls")
title_printer()

# =========================================================
# 0: two random numbers are generated and stored in a list.
# =========================================================

rand_list_of_celebs = random.sample(range(1, 8), 2)

# print(mylist)

# =========================================================
# 1: functionY computes the answer for 1,5 and returns it.
# =========================================================


def more_finder(dict_key_1, dict_key_2):
    followers_of_first_celeb = 0
    followers_of_second_celeb = 0
    name_of_first_celeb = holdict[dict_key_1]["name"]
    name_of_second_celeb = holdict[dict_key_2]["name"]
    followers_of_first_celeb = holdict[dict_key_1]["followers"]
    followers_of_second_celeb = holdict[dict_key_2]["followers"]
    # print(f"name={name_of_first_celeb}, followers={followers_of_first_celeb}")
    # print(f"name={name_of_second_celeb}, followers={followers_of_second_celeb}")
    if followers_of_first_celeb > followers_of_second_celeb:
        # print(f"{name_of_first_celeb} had more followers than {name_of_second_celeb}")
        result = name_of_first_celeb
    if followers_of_first_celeb < followers_of_second_celeb:
        # print(f"{name_of_second_celeb} had more followers than {name_of_first_celeb}")
        result = name_of_second_celeb
    print(f"result={result}")
    return result


# answer=more_finder(rand_list_of_celebs[0],rand_list_of_celebs[1])


# =============================================================
# 2: functionX asks the question and returns user input/choice
# =============================================================

def question_asker(dict_key_1, dict_key_2):

    nofc = holdict[dict_key_1]["name"]
    nosc = holdict[dict_key_2]["name"]
    fdofc = holdict[dict_key_1]["field"]
    fdosc = holdict[dict_key_2]["field"]
    lofc = holdict[dict_key_1]["location"]
    losc = holdict[dict_key_2]["location"]
    flfc = holdict[dict_key_1]["followers"]
    flsc = holdict[dict_key_2]["followers"]
    print(f"====================================")
    print(f"{nofc} a {fdofc} from {lofc} ")
    vs_printer()
    print(f"{nosc} a {fdosc} from {losc} ")
    print(f"====================================")
    choice = input("who do you think has more followers??? (enter the name): ")

    return choice


# choice=question_asker(rand_list_of_celebs[0],rand_list_of_celebs[1])


# =============================================================
# 3: Answers are compared for functionX and functionY.
# =============================================================

# if answer == choice:
#    print("You Nailed it !!!!")

# else:
#    print("Sorry, wrong answer.")


# =============================================================
# 4: Game Play
# =============================================================
answer = ""
choice = ""
counter = 0
while (answer == choice):

    os.system("cls")
    title_printer()
    print(f"Current Score is {counter}")
    rand_list_of_celebs = random.sample(range(1, 8), 2)
    answer = more_finder(rand_list_of_celebs[0], rand_list_of_celebs[1])
    choice = question_asker(rand_list_of_celebs[0], rand_list_of_celebs[1])

    if answer != choice:
        print("Sorry, wrong answer, You lose.")
        print("## GAME OVER ##.")
        break
    if answer == choice:
        print("You Nailed it !!!!")
        counter += 1

    # print(f"you have answered {counter} correct so far..")
