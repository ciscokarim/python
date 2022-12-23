# #printing full list
# numbers = ["zero","one", "two", "three", "four"]
# numstrings = ["0","1","2","3","4","5"]
# digits = [0,1,2,3,4,5]
# random = [5,10,15,20,25,30]

# print (numbers)
# print (numstrings)
# print (digits)

# #printing place values
# print(numbers)
# print(numbers[0],numbers[1],numbers[-1])
# numbers[2]="2"
# print(numbers)

# #extending lists i.e. adding another list to your lists

# # random.extend(numstrings)
# # print random

# #appending data to the end of the lists

# random.append("35")
# print random

# #entering data into the list at a position of choice

# random.insert(0,0)
# print random

# random.remove(0)
# print random

# #this doesnt work in this version
# # random.clear()
# # print random

# #this rmeoves the last element from the list
# random.pop()
# print random

# #finding the index value of an item in the lists
# print(random.index(25))

# #find how many times an item appeared in the lists
# print(random.count(5))

# # #sort alphabets or numbers in a lists
# # numbers.sort()
# # print numbers

# #reverse the order of the items
# random.reverse()
# print random

# #copying to another list
# random2=random
# print random2

# #2d lists

# list2d=[["a","b","c"],["d","e","f"],["g","h","i"]]
# print list2d[0][0],list2d[0][1],list2d[0][2]
# print list2d[1][0],list2d[1][1],list2d[1][2]
# print list2d[2][0],list2d[2][1],list2d[2][2]


# mylist1=["one","two"]
# mylist2=["three","four"]
# mylistall=[mylist1,mylist2]
# print(mylistall)

# #replace item in a list by slicing the list and adding an item in the middle.
# # find the index "b"
# charloc = mylist.index("b")
  
# # replace "b" with "k" by slicing the list and adding k in the middle.
# mylist = mylist[:charloc]+["k"]+mylist[charloc+1:]

# testlist=[]

# for numbers in range (1,11):
#     testlist+=str(numbers)

# print(testlist)

# #get the position and print the items on those positions.
# mylist=["a","b","c"]
# lml=len(mylist)
# for i in range (0,lml):
#     print(mylist[i])

# #replacing a character at a certain point in a list
# mylist[1]="k"
# print(mylist)

mylist=[

'''
  _______
     |   |
         |
         |
         |
  =============''',
    '''
  _______
     |   |
     0   |
         |
         |
  =============''',
    '''
  _______
     |   |
     0   |
    /    |
         |
  =============''',
    '''
  _______
     |   |
     0   |
    / \  |
         |
  =============''',

    '''
  _______
     |   |
     0   |
    /|\  |
         |
  =============''',

    '''
  _______
     |   |
     0   |
    /|\  |
    /    |
  =============''',

    '''
  _______
     |   |
     0   |
    /|\  |
    / \  |
  =============''',


  ]

# for items in mylist:
#     print(items)

print(mylist[3])


# def flatten(lis):
#      for item in lis:
#          if isinstance(item, Iterable) and not isinstance(item, str):
#              for x in flatten(item):
#                  yield x
#          else:        
#              yield item
# def depth_of_list(l):
#     if isinstance(l, list):
#         return 1 + max(depth_of_list(item) for item in l)
#     else:
#         return 0

# def flatten(lst):
#     for el in lst:
#         if isinstance(el, list):  # N.B. this only works for lists, not general
#                                   # collections e.g. sets, tuples, dicts, etc...
#             # recurse
#             yield from flatten(el)
#         else:
#             # generate
#             yield el
            
# mylist1=["zero1","one1","two1","three1","four1"]
# mylist2=[[["zero2","one2","two2","three2","four2"]]]

# if "zero1" in mylist1:
#     print("present in 1")

# mylist3=flatten(mylist2)
# if "zero2" in mylist3:
#     print("present in 2")
# print(mylist1[0])
# print(mylist1[1])

# if(mylist1[3]=="three1"):
#     mylist1[3]="teen1"


# print(list(flatten(mylist2)))
# print(depth(mylist2))

# dlevel=depth(mylist2)
# print(dlevel)
# mylist2_flat = []
# while (dlevel != 0):
#   dlevel-=1
#   for items in mylist2:
#     for values in items:
#       mylist2_flat.append(values)


# print(dlevel)
# print(mylist1)
# print(mylist2)
# print(mylist2_flat)
# print(mylist2_flat)






