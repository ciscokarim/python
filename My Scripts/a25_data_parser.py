# program to read files and extract data

file = open("asa221.conf", "r")
lines = file.readlines()
file.close()

yescounter = 0
nocounter = 0

print ("\nlines with NO are below:")

for line in lines:

    if line.find("NO")!=-1:
        print (line.strip())

print("\nlines with YES are below:")

for line in lines:

    if "YES" in line:
        yescounter+=1
        print (line.strip())
print ("The number of lines with YESES were: " + str(yescounter))

print("\nlines with YES and NO are below:")

for line in lines:

    if "YES" in line and "NO" in line:
        print (line.strip())

print("\nlines without NO are below:")

for line in lines:

    if "NO" not in line:
        print (line.strip())


print("\nlines with YES in any shape are below:")

for line in lines:

    if "YES" in line.upper():
        print (line.strip())


print("\nlines with YES or two:")

for line in lines:
    if "YES" in line or "two" in line:
        print (line.strip())

print("\nlines with just *YES* :")

for line in lines:
    if "YES" not in line:
        print (line.strip())

