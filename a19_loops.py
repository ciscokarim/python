#while loops

#print a table using while loop
i=1
while i<=10:
    print ("2x1="+str(2*i))
    i=i+1
print ("\n Out of loop, job done")

#'guess a secret word with a counter using while and if'

secret="the-one"
guess="guess"
counter=0
while guess!=secret and counter<=4:
    guess=input("enter the secret word: ")
    counter=counter+1
    if counter==5:
        print ("sorry you used all your tries")
    if guess==secret:
        print ("you got it")

#guess a secret word with a counter, while, if, else and boolean

secret="the-one"
guess="guess"
counter=0
at_guess_limit=False
guess_limit=4

while guess!=secret and at_guess_limit==False:
    guess=input("enter the secret word: ")
    counter=counter+1
    if counter==guess_limit:
        print ("sorry you used all your tries")
        at_guess_limit=True
    if guess==secret:
        print ("you got it")

#simple for loop with number range

for number in range (1,11):
    print (number,end="")
print ("")

#simple for loop with top range item
for number in range (11):
    print (number,end="")
print ("")

#for loop with strings

for character in "123456789":
    print (character,end="")
print ("")

for character in "abcdef":
    print (character)
print ("")

#for loop with lists

mylist=["one","two","three","four","five"]
for item in mylist:
    print (item)

mylist=[1,2,3,4,5]
for item in mylist:
    print (item)

list2d=[["a","b","c"],["d","e","f"],["g","h","i"]]
for item in list2d:
    print (item)


#for loop with index numbers
index=0
mylist=["one","two","three","four","five","six","seven","eight","nine","ten"]
for index in range(0,4):
    print (mylist[index])

#for loop with string condition
mylist=["one","two","three","four","five","six","seven","eight","nine","ten"]
for words in mylist:
    print (words, end=",")
    if (words=="five"):
        break
print ("")

#for loop with dictionaries

numberdefs = {
"0": "Zeroth number",
"1": "first number",
"2": "second number",
"3": "third number",
"4": "fourth number",
}

#following only prints keys not the definitions
for keys in numberdefs:
    print (keys, end=",")
print ("")


for definitions in numberdefs.values():
    print (definitions, end=",")
print ("")

###2d lists

#print 2d lists with nested loops

list2d= [
["a","b","c"],
["d","e","f"],
["g","h","i"]
]

for i in range (3):
   for j in range (3):
       print (list2d[i][j], end=",")
print ("")

#incomplete at 3:01:58
##if statement to look for a character in string and replace it
#
# mystring="the quick brown fox jumps right over the lazy dog"
# replacer=""
# for character in mystring:
#     if character in "AEIOUaeiou": ##instaed of using many character=="a" or etc etc
#         replacer=replacer+"*"
#         print (replacer)
#
# #     else:
# #         replacer=replacer+character
# #
# # print (mystring)
