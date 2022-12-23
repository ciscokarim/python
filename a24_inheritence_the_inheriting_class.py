#a child class will import the functionality from the parent class
#this way you dont have to copy/paste the lines from the
#parent class functions to child class functions

#import the class from another file first
from a24_inheritence_the_parent_class import dateprinter_parent

#we want to use the functionality of dateprinter_parent
#inside the dataprinter_child class
#in case of a conflicting/same definition
#parent class will take priority.
#in that case simply define that function in child
#if local def is available it wont go remote

class dateprinter_child(dateprinter_parent):
    def hk(self):
        print ("the date of birth is 2011")
    def zk(self):
        print ("the date of birth is 2013")
    def ik(self):
        print ("the date of birth is 2015")


#print using the remote, parent class
mydateprinter1=dateprinter_parent()
mydateprinter1.ak()
mydateprinter1.bk()
mydateprinter1.nk()
mydateprinter1.sk()
mydateprinter1.fk()

print ("\n")

#print using the local, child class
mydateprinter2=dateprinter_child()
mydateprinter2.hk()
mydateprinter2.zk()
mydateprinter2.ik()
