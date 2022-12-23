#classes are just like data types ie.. strings/lists/numbers
#but these are complex like students, cars, mobiles
#it is just like a template

class car:
    def __init__(self, make,year,model,colour,fuel,transmission):
        self.make = make
        self.year = year
        self.model= model
        self.colour=colour
        self.fuel=fuel
        self.transmission=transmission


#a calss function is a fucntion that is accessible to the class objects
#and it performs a specific function on the objects. make sure its aligned
#with the class definition def to def in terms of indent

    def ulzecheck(self):
        if self.year <=2011:
            return True
        else:
            return False

#un comment the following and it will be a complete class and object example
#object definited and attributes printed
# car1=car("toyota",2010,"carina","red","diesel","auto")
# print (car1.make)
# print (car1.model)
# print (car1.year)
# print (car1.fuel)
# print (car1.transmission)
# print (car1.colour)
#
# #class function called to perform a function on attributes
# print(car1.ulzecheck())
