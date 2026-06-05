student={"Name":"Yathurshika","Age":20,"Score":87,"City":"Jaffna","Is_Student":True}
for x,y in student.items():
    print(x,":",y)
student["Score"]=78
student["Grade"]="A"
del(student["Is_Student"])
print(student)