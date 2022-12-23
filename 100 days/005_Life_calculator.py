c_age=input("Enter your current age: ")
t_age=70
t_days=t_age*365
c_days=int(c_age)*365
r_days=t_days-c_days
r_weeks=r_days//7
r_months=r_days//30

print(f"you have {r_days} days, {r_weeks} weeks and {r_months} months left in your life")
