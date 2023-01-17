class user:
    
    def __init__(self,user_id,user_name,user_age,user_sex):
        self.uid=user_id
        self.uname=user_name
        self.uage=user_age
        self.usex=user_sex
        self.UADD="UK" # a contant, which dont have to be passed but can be used.
        self.UDEP="IT"

user1=user("0001","Tom Cruise","41","male")
user2=user("0002","Kevin Costner","45","male")

print(user1.uid)
print(user2.uid)
print(user1.uname)
print(user2.uname)
print(user1.UADD)

class car:
    def __init__(self):
        self.colour
        self.make


car1=car()
car1.colour="black"
car1.make="bmw"
car2=car()
car2.colour="blue"
car2.make="toyota"

print(car1.make)
print(car2.make)

