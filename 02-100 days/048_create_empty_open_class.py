class user: # defines a new empty/open class
    pass

user1 = user()  #creates an object from the class.

#because the class is open so you can define any object and name it anything with a dot.
#you can use this trick to define objects with the same prefix i.e user1, user2 etc.
#which is otherwise not possible normally.

user1.id="1234"
user1.age=24
user1.address="huddersfield"
user1.nationality="british"
user1.sex="male"

print(user1.address)
print(user1.age)
print(user1.sex)

#user2.age = 4    #if you uncomment this line and run it it will error, because user2.age is not defined
                  #and it is not part of a class.