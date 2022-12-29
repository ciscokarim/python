import random
import os


random_number=random.randint(1,100)
print(f"random_number={random_number}")
answer=0
choice="empty"
counter=10

#http://patorjk.com/software/taag/#p=display&v=0&f=Big&t=Can%20you%20Guess%3F%3F  
#above is where i got the following text converted from.

print('''
   _____                                   _____                    ___ ___  
  / ____|                                 / ____|                  |__ \__ \ 
 | |     __ _ _ __    _   _  ___  _   _  | |  __ _   _  ___  ___ ___  ) | ) |
 | |    / _` | '_ \  | | | |/ _ \| | | | | | |_ | | | |/ _ \/ __/ __|/ / / / 
 | |___| (_| | | | | | |_| | (_) | |_| | | |__| | |_| |  __/\__ \__ \_| |_|  
  \_____\__,_|_| |_|  \__, |\___/ \__,_|  \_____|\__,_|\___||___/___(_) (_)  
                       __/ |                                                 
                      |___/                                                  
''')

print(f"### You have to guess a number between 1 and 100 ###")
while(answer!=random_number):
   answer=int(input("Make a guess :"))
   # if (random_number>answer):
   #    distance=random_number-answer
   # if (answer>random_number):
   #    distance=answer-random_number

   distance=answer-random_number
   print(f"distance={distance}")
   
   if distance <= 5 and distance > 0:
      print(f"bit high, you are close")
   if distance > 5 and distance <= 10:
      print(f"high")
   if distance > 10:
      print(f"too high")       
   if (distance >= -5 and distance <= 0):
      print(f"bit low, you are close")
   if (distance < -5 and distance >= -10):
      print(f"low")
   if (distance < -10):
      print(f"too low")
   counter-=1
   
   if answer==random_number:
      print(f"You nailed it !!WELL DONE!!")
      break
   if counter>0:
      print(f"you have {counter} attempts left.")
   if counter==0:
      print(f"you have run out of attempts, !!GAME OVER!!")



# ucl=[] #user card list
# ccl=[] #computer card list

# # sum_less_than_22=False
# # while(sum_less_than_22==False):
# #    for i in range (1,3):
# #       random_card=random.randint(1,13)
# #       ucl.append(random_card)
     
# #    usum=ucl[0]+ucl[1]
# # #    print(f"sum is {sum} of {ucl}")
# #    if usum<22:
# #       sum_less_than_22=True
# #     #   print(f"sum is less than 22")
# #    else: 
# #        ucl=[]
# #        continue   


# # sum_less_than_21=False

# # while(sum_less_than_21==False):
# #    for i in range (1,3):
# #       random_card=random.randint(1,13)
# #       ccl.append(random_card)
     
# #    csum=ccl[0]+ccl[1]
# # #    print(f"sum is {sum} of {ccl}")
# #    if csum<21:
# #       sum_less_than_21=True
# #     #   print(f"sum is less than 21")
# #    else: 
# #        ccl=[]
# #        continue  


# # hccl=[ccl[0],"#"]

# # # print(ccl)
# # # print(hccl)
# # # print(ucl)

# # os.system("cls")

# # print(f"Dealers cards are >> {hccl[0]} & {hccl[1]} << with a total of {hccl[0]}")
# # print(f"Your cards are    >> {ucl[0]} & {ucl[1]} << with a total of {usum}")
# dywp=input("Do you want to play black jack ?? (yes/no) :")
# while dywp=="yes":
#    ucl=[] #user card list
#    ccl=[] #computer card list

#    sum_less_than_22=False
#    while(sum_less_than_22==False):
#       for i in range (1,3):
#          random_card=random.randint(1,13)
#          ucl.append(random_card)
      
#       usum=ucl[0]+ucl[1]
#    #    print(f"sum is {sum} of {ucl}")
#       if usum<22:
#          sum_less_than_22=True
#       #   print(f"sum is less than 22")
#       else: 
#          ucl=[]
#          continue   


#    sum_less_than_21=False

#    while(sum_less_than_21==False):
#       for i in range (1,3):
#          random_card=random.randint(1,13)
#          ccl.append(random_card)
      
#       csum=ccl[0]+ccl[1]
#    #    print(f"sum is {sum} of {ccl}")
#       if csum<21:
#          sum_less_than_21=True
#       #   print(f"sum is less than 21")
#       else: 
#          ccl=[]
#          continue  


#    hccl=[ccl[0],"#"]

#    # print(ccl)
#    # print(hccl)
#    # print(ucl)

#    os.system("cls")

#    # print(f"Dealers cards are >> {hccl[0]} & {hccl[1]} << with a total of {hccl[0]}")
#    # print(f"Your cards are    >> {ucl[0]} & {ucl[1]} << with a total of {usum}")   
#    os.system("cls")
#    print(f"Dealers cards are >> {hccl[0]} & {hccl[1]} << with a total of {hccl[0]}")
#    print(f"Your cards are    >> {ucl[0]} & {ucl[1]} << with a total of {usum}")
#    if usum==21:
#       print("Youve hit the black jack, you won")
#    else: 
#       users_choice=input("Do you want to *stand* or *hit* : ")

#       # print(csum)
#       #==================================================================================

#       if users_choice=="hit":
#          # print("Time to Show..........")
#          # print(f"Dealers cards are >> {ccl[0]} & {ccl[1]} << with a total of {csum}")
#          # print(f"Your cards are    >> {ucl[0]} & {ucl[1]} << with a total of {usum}")
         
#          # if csum == usum:
#          #    print(f"its a draw!!!")
#          # if csum > usum:
#          #    print(f"Dealer wins!!!!")
         
#          while users_choice=="hit":
#             random_card=random.randint(1,13)
#             ucl.append(random_card)
#             print(f"you take out *{random_card}*")
            
#             usum=0
#             for x in range(0,len(ucl)):
#                #print("in for loop")
#                #print(f"x is {x}")
#                usum=usum+ucl[x]
#                # print(ccl)

#             print(f"your cards are {ucl} with a total of {usum}")   

#             if usum==21:   
#                print(f"You win!!! as your total equals 21")
#                users_choice="end"

#             if usum>21:   
#                print(f"Dealer wins!!! as your total {usum} exceeded 21")
#                users_choice="end"
         
#             if usum<21:
#                users_choice=input("Do you want to *stand* or *hit* : ")
            
            
#       #==================================================================================

#       if users_choice=="stand":
#          print("Time to Show..........")
#          print(f"Dealers cards are >> {ccl} << with a total of {csum}")
#          print(f"Your cards are    >> {ucl} << with a total of {usum}")
         
#          if csum == usum:
#             print(f"its a draw!!!")
#          if csum > usum:
#             print(f"Dealer wins!!!!")
         
#          if usum > csum:
#             # while (csum<=21 and csum<usum):
#             while (csum<17):
#                # print("in while loop")
#                random_card=random.randint(1,13)
#                ccl.append(random_card)
#                print(f"dealer takes out *{random_card}*")
#                csum=0
#                for x in range(0,len(ccl)):
#                   # print("in for loop")
#                   # print(f"x is {x}")
#                   csum=csum+ccl[x]
#                   # print(ccl)
#                if csum>16:
#                   break
#             if len(ccl)>2:
#                print(f"Dealers final cards are >> {ccl} << with a total of {csum}")
#                print(f"Your  final   cards are >> {ucl} << with a total of {usum}")
#             if csum>21:
#                print(f"you win!!! as dealers total {csum} exceeded 21")
#             if csum==usum:
#                print(f"its a draw!!! ")
#             if csum<=21 and csum>usum:
#                print(f"Dealer wins!!! as the dealers sum {csum} is still within 21 limit")
#             if csum<21 and csum<usum:
#                print(f"you win!!")
   
#    dywp=input("Do you want to play another game?? (yes/no) :")