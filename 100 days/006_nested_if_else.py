age=float(input("Enter your age: "))
height=float(input("Enter your height :"))
print(f"your age is {age}")
print(f"your height is {height}")

if (age >= 18 ):
    if (height >= 1.5):
        print(f"your age is 18 or more and your height is equal or greater than 1.5, go ahead to ride")
    else:
        print(f"your age is 18 or more but your height is less than 1.5, you cannot ride")
else:
    print("Sorry!, you are under 18, you are not allowed to ride")
