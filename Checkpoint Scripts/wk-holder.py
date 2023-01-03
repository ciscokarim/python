

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






mydict={"zero":["0.0.0.0"]}     #create a dictionary with a list item in it.
mydict={"one":["1.1.1,1"]}      #add another list item to the dictionary. IT will be appended.
two="two"                       #define a key for the dictiaonry 
listtwo=["2.2.2.2"]             #define a value for the dictoinary
mydict[two]=listtwo             #add anohter list item to the dict by using the variable names.
mydict["three"]=["3.3.3.3"]     #add another list item to the dict 
mydict["two"].extend(["22.22.22.22"])   #add another item to the list within the dictionary. not the dict.
print(f"dictionary is ....")        
print(f"{mydict}")
print(f"keys are ..")
print(mydict.keys())    #print the dict keys
print(f"values are ")
print(mydict.values())  #print the dict values for the kyes
print(f"key at 1 is")
print(list(mydict)[0])  #access the first list in the dictionary.
print(f"value at 1,0 is")
print(list(mydict.values())[1][0]) #access the first value in the first list of the dictionary.
print(f"value at 1,1 is")
print(list(mydict.values())[1][1]) #access the second value in the first list of the dictionary.





