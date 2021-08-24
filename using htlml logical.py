student_name=['swapna','shailu','laxmi','neelu']
students_age=[21,22,20,21]
qualificatio=['bsc','degree','btec','inter']
with open("student_det","w") as f1:
    f1.write("<!Doctype html>\n")
    f1.write("<html>\n")
    f1.write("<head>\n")
    f1.write("<title> STUDENT DETAILS<\title>\n")
    f1.write("<\head>\n")
    f1.write("<body>\n")
    f1.write("<ul>\n")
    for name in student_name:
        dic={}
        dic['name']=name
    for age in students_age:
        dic['age']=age
    for study in qualificatio:
        dic["qualification"]= study
    
        f1.write("<li>")
        f1.write(str(dic))
        f1.write("<\li>\n")
    f1.write("<\body>\n")
    f1.write("<\html>")

