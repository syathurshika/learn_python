contact={"Suresh":"0777009889","Thena":"0779228958","Yathurshika":"0775509959","Pravin":"0712193600"}

name=input("Enter the name: ")
for x,y in contact.items():
    if name==x:
        print(f"The contact number of {name} is {y}")
        break
else:  
    print("Name not found in contact list")