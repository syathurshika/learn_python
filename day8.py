#task1
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

# task2
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    bmi = round(bmi, 2)
    return bmi
calculate_bmi(weight, height)

bmi = calculate_bmi(weight, height)

if bmi < 18.5:
    bmi_category = "Underweight"
elif 18.5 <= bmi < 24.9:
    bmi_category = "Normal weight"
elif 25 <= bmi < 29.9:
    bmi_category = "Overweight"
else:
    bmi_category = "Obese"

print(f"Your BMI is {bmi} and your category is {bmi_category}.")