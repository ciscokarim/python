# global the_list
# mylist=["one","two","three","four","quit"]

def menu_generator(the_list):
    option=0
    while (option < len(the_list)):
        for index,item in enumerate(the_list):
            print(f"[{index+1}] {item}")

        option=int(input("Enter the option you want :"))
        
        if option < 1 or option > len(the_list):
            print("number out of range, Please try again.")
            option=int(input("Enter the option you want :"))

        if option == len(the_list):
            print("Good Bye")

        # print (f"you selected option {option}, {the_list[option-1]}")
    return the_list[option-1]

# option_selected=menu_generator(mylist)
# print(f"option selected = {option_selected}")


