import json

with open("7_15_02_23_show_hosts.json") as json_objects1_file:
    python_objects1_list = json.load(json_objects1_file)

# with open("objects2.json") as json_objects2_file:
#     python_objects2_dict = json.load(json_objects2_file)

print(type(python_objects1_list))
print(len(python_objects1_list))
# print(python_objects1_list)


for each_dict in python_objects1_list:
  # print(f'name: {each_dict["name"]}  ,,,,  ip: {each_dict["ipv4-address"]}   ')
  print(f'{each_dict["name"]},{each_dict["ipv4-address"]},')
  

# print(type(python_objects2_dict))
# print(python_objects2_dict)

# del python_objects1_dict["from"]
# del python_objects1_dict["to"]
# del python_objects1_dict["total"]

# del python_objects2_dict["from"]
# del python_objects2_dict["to"]
# del python_objects2_dict["total"]

# print(type(python_objects1_dict))
# print(python_objects1_dict)

# print(type(python_objects2_dict))
# print(python_objects2_dict)

# # list_holder1 = []

# new_dict = python_objects1_dict | python_objects2_dict

# print(new_dict)


# def merge_two_dicts(x, y):
#     z = x.copy()   # start with keys and values of x
#     z.update(y)    # modifies z with keys and values of y
#     return z


########################################################################
#combing using lists

# list_holder1 = python_objects1_dict["objects1"]

# for items in list_holder1:
#   print (items)

# list_holder2 = python_objects2_dict["objects2"]

# for items in list_holder2:
#   print (items)

# combined_list = list_holder1 + list_holder2

# print (combined_list)


# list1 = [1,2,3,4,5]
# list2 = [7,8,9,10]

# list3 = list1 + list2

# print(list3)

# strlist3= str(list3)
# with open("listtest.txt", "a") as listfile:
#   # list_file_holder = list_file_holder.write(listfile)
#   listfile.write(strlist3)
