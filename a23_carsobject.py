# #object is an instance or a live example of the class
#

from a23_carsclass import car

car1=car("toyota",2010,"carina","red","diesel","auto")
car2=car("audi",2011,"a4","black","petrol","man")
car3=car("bmw",2012,"m3","blue","electric","auto")

#print the individual attributes of the object

print (car1.make)
print (car1.year)
print (car1.model)
print (car2.make)
print (car2.model)
print (car2.year)

#use the function the class to get certain
#information about the objects ulzecheck is a
#class function defined under class

print ("is it ulze compliant: "+str(car1.ulzecheck()))
