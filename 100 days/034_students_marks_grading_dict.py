###########################################################################
# find the highest grader.
###########################################################################
students_grades={}
students_marks={"st1":40,"st2":90,"st3":87,"st4":70,"st5":35}
for key,value in students_marks.items():
    if value<40:
        students_grades[key]="fail"
    if value>=40 and value<60:
        students_grades[key]="pass"
    if value>=60 and value<70:
        students_grades[key]="good"
    if value>=70 and value<80:
        students_grades[key]="very good"
    if value>=80 and value<90:
        students_grades[key]="excellent"
    if value>=90 and value<100:
        students_grades[key]="Distinction"

print(students_grades)