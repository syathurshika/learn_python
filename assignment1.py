#Step1-Collecting Inputs
name = input("Enter your full name: ")
age = int(input("Enter your age: "))
score = int(input("Enter your exam score (0-100): "))
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

#Step2-Printing the student's profile
print("===== STUDENT PROFILE =====")
print("Name : ",name ,type(name))
print("Age : ",age ,type(age))
print("Score : ",score ,type(score))
print("Weight : ",weight,"kg", type(weight))
print("Height : ",height,"m", type(height))
print("===========================")

#Step3-Calculating and displaying results
bmi = weight / (height ** 2)
bmi = round(bmi, 2)
birth_year = 2025 - age
passed = score >= 50
even_or_odd = age % 2 == 0

#Step4a-Exam Grade
if score < 0 or score > 100:
    print("Invalid score entered.")
else:
    if score >= 90:
        grade = "A"
        grade_message = "Outstanding! You are a top student."
    elif score >= 80:
        grade = "B"
        grade_message = "Great work! Keep pushing higher."
    elif score >= 70:
        grade = "C"
        grade_message = "Good effort. A little more focus will do it."
    elif score >= 60:
        grade = "D"
        grade_message = "You passed. But you can do better."
    else:
        grade = "F"
        grade_message = "You did not pass. Study harder and try again."

#Step4b-BMI Category
if bmi < 18.5:
    bmi_category = "Underweight"
    bmi_advice = "Consider eating more nutritious food."
elif bmi < 25:
    bmi_category = "Normal"
    bmi_advice = "Great! Maintain your healthy lifestyle."
elif bmi < 30:
    bmi_category = "Overweight"
    bmi_advice = "Try adding more exercise to your routine."
else:
    bmi_category = "Obese"
    bmi_advice = "Please consult a doctor for a health plan."

#Step4c-Age Group
if age < 13:
    age_group_message = "You are a child. Keep learning!"
elif age < 18:
    age_group_message = "You are a teenager. Great time to start coding."
elif age < 26:
    age_group_message = "You are a young adult. Python will open many doors!"
elif age < 60:
    age_group_message = "You are an adult. It is never too late to learn."
else:
    age_group_message = "You are a senior. Inspiring dedication!"

#Step4d-Eligibility Checks
eligible_to_vote = age >= 18
healthy_passing = (bmi < 25) and passed
very_young_or_senior = (age < 18) or (age >= 60)

#Step5-Print the final personalised report
print("========================================")
print(" STUDENT SMART ADVISOR REPORT ")
print("========================================")
print("Hello,", name,"!")
print("Your exam grade : ",grade,"-" ,grade_message)
print("Your BMI : ",bmi,"-",bmi_category)
print("BMI advice : ",bmi_advice)
print("Your age group : ",age_group_message)
print("Born in : ",birth_year)
print("Eligible to vote : ",eligible_to_vote)
print("Healthy & passing : ",healthy_passing)
print("Very young/senior : ",very_young_or_senior)
print("========================================")
