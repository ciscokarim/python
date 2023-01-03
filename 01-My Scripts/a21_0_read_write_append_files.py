# filereader=open("readingfile.txt", "r")  #r is read, w is write, a is append and r+ read and write
# #print(filereader.read())  # this prints the whole filereader
# #print(filereader.readline()) # reads the first readline
# #print(filereader.readline()) # reads the second line now
# frlist = (filereader.readlines()) # this stores the file in an array/list
# #print (frlist[2]) # this now prints the line number in the array
# #or  you can put a loop to read the contents of the file know
# for items in frlist:
#     print (items)
# filereader.close()


# ################## writing to files using append (add to the end)
# filereader=open("readingfile.txt", "r")
# fileappender=open("readingfile.txt","a")
# fileappender.write("\nadd this x new line to the end of file")
# print (filereader.read())
# filereader.close()


################## writing to files using append (add to the end)
filereader=open("readingfile.txt", "r")
filewriter=open("readingfile.txt","w")
filewriter.write("\nadd this x new line to the end of file")
print (filereader.read())
filereader.close()
filewriter.close()
