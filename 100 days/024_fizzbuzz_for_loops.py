#generate even numbers
eadder=0
for num in range (1,31):
    #print(f"current value of num is {num}")

    if(num%3==0 and num%5==0):
        print("fizz buzz")
    elif(num%3==0):
        print("fizz")
    elif(num%5==0):
        print("buzz")
    else:
        print(num)
