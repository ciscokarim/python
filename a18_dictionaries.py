# #============================================================================================

# digitdefs = {

# 0: "Zeroth digit",
# 1: "first digit",
# 2: "second digit",
# 3: "third digit",
# 4: "fourth digit",

# }

# print (digitdefs) #this prints the full dictionary
# print (digitdefs[3]) # this prints the value of key 3
# print (digitdefs.get(3)) #this prints the value of key 3

# for each in digitdefs:
#     print(each)     #prints each key

# for each in digitdefs:
#     print(maskdict[each]) #prints value of each key

# for eachx,eachy in digitdefs.items():
#     print(eachx,eachy)

# #============================================================================================

# numberdefs = {

# "0": "Zeroth number",
# "1": "first number",
# "2": "second number",
# "3": "third number",
# "4": "fourth number",

# }

# print (numberdefs) #this prints the full dictionary
# print (numberdefs["3"]) # this prints the value of key 3
# print (numberdefs.get("3")) #this prints the value of key 3

# strthree=numberdefs["3"]
# print (strthree)
# strfour=numberdefs["4"]
# print (strfour)

# #============================================================================================

# ### list or any other itmes inside a dictionary
# mydict={

#     "a11":["11"],
#     "a12":["12"],
#     "a13":["13","23","33"],
#     "a14":["14","24","34","44"]
# }

# #add another item to the dictioary
# mydict['a15']=["15","25","35","45","55"]

# #updatev values of keys in a dictioary
# mydict['a15']=["15","25","35","45","55","65"]

# #print keys of dictionary
# for eachitem in mydict:
#     print (eachitem)

# #print itmes of dictionary
# for eachitem in mydict:
#     print (mydict[eachitem])

# print(mydict)
# #https://www.guru99.com/python-dictionary-append.html


# print(list(mydict.keys())[list(mydict.values()).index(["12"])])  # Prints a12
# #the above separates keys into a list and values into another one. 

# #get values and keys in a function
# print(mydict.keys())
# print(mydict.values())

# #get clean values and keys in a list
# print(list(mydict.keys()))
# print(list(mydict.values()))


# # #============================================================================================

# mydict={"zero":["0.0.0.0"]}     #create a dictionary with a list item in it.
# mydict={"one":["1.1.1,1"]}      #add another list item to the dictionary. IT will be appended.
# two="two"                       #define a key for the dictiaonry 
# listtwo=["2.2.2.2"]             #define a value for the dictoinary
# mydict[two]=listtwo             #add anohter list item to the dict by using the variable names.
# mydict["three"]=["3.3.3.3"]     #add another list item to the dict 
# mydict["two"].extend(["22.22.22.22"])   #add another item to the list within the dictionary. not the dict.
# print(f"dictionary is ....")        
# print(f"{mydict}")
# print(f"keys are ..")
# print(mydict.keys())    #print the dict keys
# print(f"values are ")
# print(mydict.values())  #print the dict values for the kyes
# print(f"key at 1 is")
# print(list(mydict)[0])  #access the first list in the dictionary.
# print(f"value at 1,0 is")
# print(list(mydict.values())[1][0]) #access the first value in the first list of the dictionary.
# print(f"value at 1,1 is")
# print(list(mydict.values())[1][1]) #access the second value in the first list of the dictionary.

# # #====================================================================================================================#

# # print(mydic.get("a13")) #this will print the corressponding value for a13 key.
# # print(bidder_dict.get("aftab")) #this will print the corressponding value for aftab key.
# # print(bidder_dict["aftab"]) #this will print the corressponding value for aftab key.

# # #following will get the key for a value in the following exmaple value is ..12
# # keys = [k for k, v in bidder_dict.items() if v == "12"]
# # print(keys)

# # #following will get the key for a value or vice versa in the following exmaple value is ..12
# # for key,value in bidder_dict.items():
# #   if key=="aftab": print (value)
# #   if value==40: print(key)

# # #====================================================================================================================#

# ###lists inside a dictionary

# cities_in_countries = {
    
# "France": ["Paris","Lille","Dijon"],
# "USA":    ["Newyork","Chicago","Dallas"],
# "UK":     ["London","Manchester","Birmingham"]

# }

# #adding another item in the dictionary.
# cities_in_countries["Germany"]=["Stuttgart","Berlin","Frankfert"]

# #extending a list in the  dictionary 
# cities_in_countries["UK"].extend(["Leeds"])

# #printing values and keys in a dictionary
# for keys,values in cities_in_countries.items():
#     print (f"keys is : {keys} and \n values are : {values}")

# #accessing second value in every dictionary
# for keys,values in cities_in_countries.items():
#     print(f"second item in each value list is {values[1]}") 

# # #====================================================================================================================#
# #Nested Dictionaries (list in a dictionary within a dictionary )   dict(dict(list))

# from ast import Delete


# countries = {

# "France": {"cities":["Paris","Lille","Dijon"],            
#            "Language":["French"],                    
#            "Population":100000000},

# "USA":    {"cities":["Newyork","Chicago","Dallas"],
#            "Language":["English","French","Spanish"],
#            "Population":300000000},

# "UK":     {"cities":["London","Manchester","Birmingham"],
#            "Language":["English","Welsh"],          
#            "Population":100000000}
# }

# # print(countries)

# #add another item=dictinary) to the dictionary
# countries["Italy"] =     {  
#                             "cities":["Milan","Rome","Vetican"],
#                             "Language":["Italian"],          
#                             "Population":100000000
#                          }

# #add another item=key&value to the dictionary
# countries["Italy"]["area"] = 12345

# ##edit a single item
# countries["Italy"]["Language"]=["Italian","Swiss"]
# print(countries["Italy"])    

# ##delete a single item (key and its value)
# del countries["Italy"]["area"]
# print(countries["Italy"])  

# ##delete a single item (key and its specific value)
# del countries["Italy"]["Language"][1]
# print(countries["Italy"])


# ##access each dictionary key individually
# print(countries["UK"])
# print(countries["UK"]["cities"])
# print(countries["UK"]["Language"])
# print(countries["UK"]["Population"])

# ##access each item within the list within the dictionary
# print(countries["UK"]["cities"][0])
# print(countries["UK"]["Language"][0])

#====================================================================================================================# #
#Nested Dictionaries in a list (dictionary within a dictionary within a list )   list(dicts(list))

countries = [

        {         "France": {   "cities":["Paris","Lille","Dijon"],            
                                "Language":["French"],                    
                                "Population":100000000
                            }
        },

        {           "USA":  {   "cities":["Newyork","Chicago","Dallas"],
                                "Language":["English","French","Spanish"],
                                "Population":300000000
                            }
        
        },

        {            "UK":  {   "cities":["London","Manchester","Birmingham"],
                                "Language":["English","Welsh"],          
                                "Population":100000000
                            }
        }
]

new_country=         {"UAE":  { "cities":["Dubai","Sharjah","Al-Ain"],
                                "Language":["Arabic"],
                                "Population":300000 }}

countries.append(new_country)
print(countries)

#====================================================================================================================# #
#Nested Dictionaries in a list (dictionary within a dictionary within a list )   list(dicts(list))