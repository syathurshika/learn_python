a=int(input("Enter a number:"))
b=int(input("Enter another number:"))
def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)      
def mul(a,b):
    print(a*b)
def div(a,b):
    if b==0:
        print("Cannot divide by zero")
    else:
        print(a/b)
add(a,b)
sub(a,b)
mul(a,b)
div(a,b)