#task1
marks=[85,62,43,98,70]
for i in range(len(marks)):
    if marks[i]>=50:
        print(f"Student: {i+1} scored {marks[i]} - Pass")
    else:
        print(f"Student: {i+1} scored {marks[i]} - Fail")

print(f"Highest: {max(marks)}")
print(f"Lowest: {min(marks)}")
print(f"Average: {sum(marks)/len(marks)}")


#task2
score=[]
for i in range(5):
    score.append(int(input("Enter score:")))
print(f"Score: {score}")
print(f"Highest: {max(score)}")
print(f"Lowest: {min(score)}")
print(f"Average: {sum(score)/len(score)}")