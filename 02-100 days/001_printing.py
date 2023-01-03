print ("\n===================================\n")

print ("Day 1 - Python Print Function")
print ("The function is declared like this:")
print("print('what to print')")   

print ("\n===================================\n")

# remember to do single and double quotes if you are 
# using them both in a single statement. " cannot be used
# twice in a statement.

print ("one")
print ("two")
print ("three")

print ("\n===================================\n")

print ("one\ntwo\nthree")

print ("\n===================================\n")

print ("one"+"two"+"three")
print ("one "+"two "+"three ")

print ("\n===================================\n")

print("Day 1 - String Manipulation")
print("String Concetenation is done with the '+' sign.")
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

print ("\n===================================\n")

print ("Day 1 - String Manipulation")
print ('String concatenation is done with the "+" sign.')
print ('e.g. print("Hello " + "world"')
print ("New lines ca n be created with a backslash and n.")

print ("\n===================================\n")

##  printing shapes
print ("\n")
print ("        /\        ")
print ("       /  \       ")
print ("      /____\      ")
print ("\n")
print (" the triangle ")
print ("\n")

print ("\n===================================\n")

##  string variables

strvar1="-- first line ends here --"
strvar2="-- second line ends here --"
strvar3="-- third line ends here --"

## printing lines and string variables

print ("\n")
print ("first line of the story"+strvar1+".\n")
print ("third line of the story"+strvar3+".\n")
print ("second line of the story"+strvar2+".\n")

print ("\n===================================\n")

## number variables

numvar1=1
numvar2=2
numvar3=3

## printing number variables

print ("\n")
print ("three number variables printed together are : " + str(numvar1)+str(numvar2)+str(numvar3))

## printing number varials and lines

print ("first number varilable is : "+str(numvar1))
print ("first number varilable is : "+str(numvar2))
print ("first number varilable is : "+str(numvar3))
print ("\n")
print ("\n===================================\n")

#checking the upper or lower case of string

result=(strvar1.isupper())
print ("\n")
print ("the string is upper case = "+ str (result))
result=(strvar1.islower())
print ("the string is lower case = "+ str (result))
print ("\n")

print ("\n===================================\n")

#converting and formatting strings
print (strvar1.upper()+" changed the variable to uppercase")
print (strvar1.lower()+" changed the variable to lowercase")
print (str(len(strvar1))+" is the length of the variable")

print ("\n===================================\n")

#accessing certain values in strings using []

print ("first character in string is -- "+strvar1[0]+" --\n")
print ("second character in string is -- "+strvar1[1]+" --\n")
print ("third character in string is -- "+strvar1[2]+" --\n")
print ("fourth character in string is -- "+strvar1[3]+" --\n")
print ("fifth character in string is -- "+strvar1[4]+" --\n")
print ("sixth character in string is -- "+strvar1[5]+" --\n")
print ("seventh character in string is -- "+strvar1[6]+" --\n")

print ("\n===================================\n")

# finding the place value or index location of a letter in a string

print ("location of t in strvar1 "+strvar1+" is :"+str(strvar1.index("t"))+"\n")
print ("location of d in strvar1 "+strvar1+" is :"+str(strvar1.index("d"))+"\n")
print ("location of r in strvar1 "+strvar1+" is :"+str(strvar1.index("e"))+"\n")
print ("location of r in strvar1 "+strvar1+" is :"+str(strvar1.index("n",1,12))+"\n")
#if the value is not found between 1,12 (the range) the program will error
print ("location of *ends* in strvar1 "+strvar1+" is :"+str(strvar1.index("ends"))+"\n")

print ("\n===================================\n")

# find and replace in a strings
print("*ends* was replaced with *finishes* in the string (line) below \n")
print (strvar1.replace("ends","finishes"))

print ("\n===================================\n")