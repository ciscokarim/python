yname_ac=input("Enter your full name, as in Joe Bloggs :")
lname_ac=input("Enter your lover's name, as in Joe Bloggs :")

yname_lc=yname_ac.lower()
lname_lc=lname_ac.lower()
 
yl_name_lc=yname_lc+lname_lc

t_count_yln=yl_name_lc.count("t")
r_count_yln=yl_name_lc.count("r")
u_count_yln=yl_name_lc.count("u")
e_count_yln=yl_name_lc.count("e")
l_count_yln=yl_name_lc.count("l")
o_count_yln=yl_name_lc.count("o")
v_count_yln=yl_name_lc.count("v")
e_count_yln=yl_name_lc.count("e")

percentage_string=str(t_count_yln+r_count_yln+u_count_yln+e_count_yln)+str(l_count_yln+o_count_yln+v_count_yln+e_count_yln)
percentage_number=int(percentage_string)

print("the percentage is : "+str(percentage_number))
if (percentage_number >20 and percentage_number <50):
    print("bad love as your love is :" + percentage_string)

if (percentage_number >50 and percentage_number <100):
    print("good love as your love is :" + percentage_string)

    