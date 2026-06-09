# Student Name: [Yathurshika] | Assignment 2

# Step 1 - Functions

def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def is_pass(score):
    return score >= 60

def calculate_average(marks):
    return round(sum(marks) / len(marks), 2)

def find_highest(marks):
    return max(marks)

def find_lowest(marks):
    return min(marks)

# Step 2 - Collect student names and marks using loops

names = []
marks = []

for i in range(5):
    name = input(f"Enter name for student {i + 1}: ")
    names.append(name)

    while True:
        mark = int(input(f"Enter mark for {name} (0-100): "))
        if mark < 0 or mark > 100:
            print("Invalid mark - please re-enter")
        else:
            break

    marks.append(mark)

average = calculate_average(marks)
highest = find_highest(marks)
lowest  = find_lowest(marks)

# Step 3 - Store class information in a Dictionary

pass_count = 0
for mark in marks:
    if is_pass(mark):
        pass_count += 1

class_info = {
    "class_name":      "Python Beginners Batch 1",
    "instructor":      "Sirithar Santhosh",
    "total_students":  5,
    "class_average":   average,
    "pass_count":      pass_count,
}

best_name    = names[marks.index(highest)]
weakest_name = names[marks.index(lowest)]

top_students = (best_name, weakest_name)
best, weakest = top_students

# Step 4 - Print the full report

print("\nStudent Results:")
for i in range(len(names)):
    grade  = get_grade(marks[i])
    status = "Pass" if is_pass(marks[i]) else "Fail"
    print(f"  {i + 1}. {names[i]:<12} | {marks[i]:>3} | Grade: {grade} | {status}")

print("\nClass Info (Dictionary):")
for key, value in class_info.items():
    print(f"  {key}: {value}")

# Step 5 - Final summary report

print("\n" + "=" * 40)
print("     STUDENT MARKS MANAGER REPORT")
print("=" * 40)
print(f"Class      : {class_info['class_name']}")
print(f"Instructor : {class_info['instructor']}")
print(f"Students   : {class_info['total_students']}  |  Passed: {class_info['pass_count']}")
print("-" * 40)
print("Student Results:")
for i in range(len(names)):
    grade  = get_grade(marks[i])
    status = "Pass" if is_pass(marks[i]) else "Fail"
    print(f"  {i + 1}. {names[i]:<12} | {marks[i]:>3} | Grade: {grade} | {status}")
print("-" * 40)
print(f"Class Average : {class_info['class_average']}")
print(f"Highest Mark  : {highest}  ({best})")
print(f"Lowest Mark   : {lowest}  ({weakest})")
print("=" * 40)
