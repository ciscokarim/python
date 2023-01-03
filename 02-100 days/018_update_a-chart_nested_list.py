row1=["r11","r12","r13","r14"]
row2=["r21","r22","r23","r24"]
row3=["r31","r32","r33","r34"]
rowall=[row1,row2,row3]

point=input("Enter the location you want to replace as in row&col e.g. 21 : ")

rownum=int(point[0])
colnum=int(point[1])
rowall[rownum-1][colnum-1]="  X"

for items in rowall:
    print(items)