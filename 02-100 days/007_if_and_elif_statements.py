age=float(input("Enter your age: "))

if (age >= 18 ): #all of the below will be by passed .. if this is true
    print(f"over 18, pays 20£")
elif (age <=18 and age >=12):
    print(f"over 12 and under 18, pays 15£")
elif (age <=12 and age >=8):
    print(f"over 8 and under 12, pays 10£")
elif (age <=12 and age >=8):
    print(f"over 8 and under 12, pays 5£")
elif (age <=10 and age >=5):
    print(f"over 5 and under 10, pays 3£")
else:
    print(f"under 5 go free")
