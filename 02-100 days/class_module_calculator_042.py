#classes are just like data types ie.. strings/lists/numbers
#but these are complex like students, cars, mobiles
#it is just like a template

class calculator:
    def __init__(self, num1, num2):  #this function is called evertime an object is created or used from this class.
        self.num1 = num1             #these are attributes of the class/ variables.
        self.num2 = num2             #only variables with names self.X will be visiable and used below 
                                     #by the functions/methods.   

#a calss function is a fucntion that is accessible to the class objects
#and it performs a specific function on the objects. make sure its aligned
#with the class definition def to def in terms of indent

    def adder(self):
        return self.num1+self.num2

    def subtractor(self):
        return self.num1-self.num2
    
    def multiplier(self):
        return self.num1*self.num2

    def divider(self):
        return self.num1/self.num2

    def power(self):
        return self.num1**self.num2

#uncomment the following and it will be a complete class and object example
#object defined and attributes printed
# calculator1=calculator(8,2)
# print(calculator1.num1)
# print(calculator1.num2)
# print(calculator1.adder())
# print(calculator1.multiplier())
# print(calculator1.power())