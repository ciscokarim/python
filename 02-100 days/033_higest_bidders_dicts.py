###########################################################################
# find the highest bidder.
###########################################################################
#Steps
#hold bidder name
#hold bid's amount
#append the bidder's name and amount to a dictionary.
#ask if there are any more bidders.
#if there are repeat.
#if there arent get out of the while loop.
#at this stage you should have a full list of bidders and their amounts.

#go through the values and find the highest value.
#find the corresponding key from the list of names.
#Tell the user the result of the highest bid.
import os
bidder_dict={}
# bidder_dict={"aftab":40,"basit":35,"faizan":42,"nada":39}
any_more_bidders=""

while (any_more_bidders!="no"):
    bidder_name=input("What is the bidders name: ")
    bid_amount=int(input("What is the bid's amount: "))
    bidder_dict[bidder_name]=bid_amount
    any_more_bidders=input("Any more Bidders :")
    os.system("cls")

lobd=len(bidder_dict)

holder=0
for i in range (0,lobd):
    if(list(bidder_dict.values())[i]>holder):
        holder=list(bidder_dict.values())[i]
        key=list(bidder_dict.keys())[i]
#print(f"holder is {holder} and key is {key}")
#print(bidder_dict)
#print(bidder_dict.items())
# highest_bidder=list(bidder_dict)[holder]
print(f"the highest bidder was {key} with the bid amount of £{holder}")

# print(bidder_dict.get("aftab"))
# print(bidder_dict["aftab"])

# keys = [k for k, v in bidder_dict.items() if v == 42]
# print(keys)