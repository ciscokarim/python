print ("hello")


##  printing shapes

print ("        /\        ")
print ("       /  \       ")
print ("      /____\      ")

print (" the triangle ")

##  printing lines (consecutive)

print ("\n")
print ("\t")
print (r"\n")
print (r"\t")
print ("first line of the story")
print ("second line of the story")
print ("third line of the story")

##  string variables

strvar1=", first line ends here"
strvar2=", second line ends here"
strvar3=", third line ends here"


## printing lines and string variables


print ("\n")
print ("first line of the story"+strvar1+".\n")
print ("third line of the story"+strvar3+".\n")
print ("second line of the story"+strvar2+".\n")

## number variables

numvar1=1
numvar2=2
numvar3=3

## printing number variables

print ("\n")
print (str(numvar1)+str(numvar2)+str(numvar3))

## printing number varials and lines

print ("\n")
print ("first line of the story" +strvar1+". "+str(numvar1)+"\n")
print ("second line of the story"+strvar2+". "+str(numvar2)+"\n")
print ("third line of the story" +strvar3+". "+str(numvar3)+"\n")


#printing " and \ and print literally anything with \

print ("\n")
print ("  \  \n")
print ("  \"  \n")

#printing a string variables

print (strvar1)
print ("\n")

#checking the upper or lower case of string

result=(strvar1.isupper())
print ("the string is upper case = "+ str (result))

print ("\n")

result=(strvar1.islower())
print ("the string is lower case = "+ str (result))


#converting and formatting strings

print ("\n")
print (strvar1.upper()+" changed the variable to uppercase\n")
print (strvar1.lower()+" changed the variable to lowercase\n")
print (str(len(strvar1))+" checked the length of the variable\n")

#accessing certain values in strings using []

print ("first character in string is "+strvar1[0]+"\n")
print ("fifth character in string is "+strvar1[4]+"\n")
print ("sixth character in string is "+strvar1[5]+"\n")
print ("seventh character in string is "+strvar1[6]+"\n")

# finding the place value or index location of a letter in a string

print ("location of t in strvar1 is :"+str(strvar1.index("t"))+"\n")
print ("location of d in strvar1 is :"+str(strvar1.index("d"))+"\n")
print ("location of r in strvar1 is :"+str(strvar1.index("r"))+"\n")

# find and replace in a strings

print (strvar1.replace("ends","finishes"))


#convert aftab to Aftab and BASIT to Basit
string="aftab"
print(string.title())