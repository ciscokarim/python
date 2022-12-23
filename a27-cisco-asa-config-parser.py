#============================================================================
#this section loads the template file and the current file

target_logging_file = open("target_logging_config.conf","r")
asa_config_file = open("asa221.conf","r")
output_file = open("output_file","w")

print("\nlines present are .....\n")
print ("================================")
target_logging_file.seek(0)
for target_lines in target_logging_file:
  asa_config_file.seek(0)
  for current_lines in asa_config_file:
    if target_lines != current_lines:
         print (target_lines.strip())

#
# print("\nlines absent are .....\n")
# print ("================================")
# target_logging_file.seek(0)
# for target_lines in target_logging_file:
#   # asa_config_file.seek(0)
#   for current_lines in asa_config_file:
#      if target_lines != current_lines:
#          print (target_lines.strip())
#          # break

# target_logging_file.close()
# asa_config_file.close()





# with open ("target_logging_config.conf","r") as target_logging_file:
#     with open ("asa221.conf","r") as current_asa_file:
#         same=set(target_logging_file).intersection(current_asa_file)
#
# print("\nlines present are .....")
# print ("================================")
# for lines in same:
#     print(lines.strip())
#
# with open("target_logging_config.conf", "r") as target_logging_file:
#     with open("asa221.conf", "r") as current_asa_file:
#         diff=set(target_logging_file).difference(current_asa_file)
#         #diff=set(target_logging_file).difference_update(current_asa_file)
#         print ("\n\n")
# print ("lines missing are ....")
# print ("================================")
#
# for lines in diff:
#     print (lines.strip())

# # program to read files and extract data
#
# file = open("asa221.conf", "r")
# lines = file.readlines()
# file.close()
#
# print ("\nlines with NO are below:")

# for line in lines:
#
#     if line.find("NO")!=-1:
#         print (line.strip())
#
# print("\nlines with YES are below:")
#
# for line in lines:
#
#     if "YES" in line:
#         yescounter+=1
#         print (line.strip())
# print ("The number of lines with YESES were: " + str(yescounter))
#
# print("\nlines with YES and NO are below:")
#
# for line in lines:
#
#     if "YES" in line and "NO" in line:
#         print (line.strip())
#
# print("\nlines without NO are below:")
#
# for line in lines:
#
#     if "NO" not in line:
#         print (line.strip())
#
#
# print("\nlines with YES in any shape are below:")
#
# for line in lines:
#
#     if "YES" in line.upper():
#         print (line.strip())
#
#
# print("\nlines with YES or two:")
#
# for line in lines:
#     if "YES" in line or "two" in line:
#         print (line.strip())
#
# print("\nlines with just *YES* :")
#
# for line in lines:
#     if "YES" not in line:
#         print (line.strip())
#
